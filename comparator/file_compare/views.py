from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import CompareForm,DoctoPdfForm,PdftoDocForm
from .models import Compare,DoctoPdf,PdftoDoc

import logging
import random


logger = logging.getLogger('django')

def home(request):
    return render(request, 'home.html')

def file_selector(request):
    
    return render(request, 'file_selector.html')

def file_list(request):
    compare_list = Compare.objects.all()
    return render(request, 'compare_list.html', {
        'file': compare_list
    })

def word_to_pdf(request):
    import pythoncom
    import win32com.client
    xl=win32com.client.Dispatch("Excel.Application",pythoncom.CoInitialize())
    from docx2pdf import convert

    if request.method == 'POST':
        form = DoctoPdfForm(request.POST, request.FILES)
        word = request.FILES["word_file"]
        if form.is_valid():
            form.save()   
            num = random.randint(1,10000)
            output = "output_file"+str(num)
            word_file = "./media/files/doc_file/"+str(word)
            pdf = "./media/files/pdf_file/"+output+".pdf"
            convert(word_file,pdf)
        else:
            messages.error(request,'Please select the word file')
            return render(request, 'word_to_file.html', {
    'form': form
    })
            
        return render(request, 'output_file.html', {
            'path':pdf
    })
    
    else:
        
        form = DoctoPdfForm()
    return render(request, 'word_to_file.html', {
    'form': form
    })

def pdf_to_word(request):
  
    #import aspose.words as aw
    from pdf2docx import Converter
    
    if request.method == 'POST':
        form = PdftoDocForm(request.POST, request.FILES)
        word = request.FILES["pdf_file"]
        if form.is_valid():
            form.save()   
            num = random.randint(1,10000)
            output = "output_file"+str(num)
            pdf_file = "./media/files/pdf_file/"+str(word)
            word_file = "./media/files/doc_file/"+output+".doc"
            # doc = aw.Document(pdf_file)
            # doc.save(word_file)
            cv = Converter(pdf_file)
            cv.convert(word_file, start=0, end=None)
            cv.close()
        else:
            # messages.error(request,'Please select the PDF file')
            return render(request, 'pdf_to_doc.html', {
    'form': form
    })
            
        return render(request, 'output_file.html', {
            'path':word_file
    })
    
    else:
        
        form = PdftoDocForm()
    return render(request, 'pdf_to_doc.html', {
    'form': form
    })



def upload_file(request):
    if request.method == 'POST':
        form = CompareForm(request.POST, request.FILES)
        print(request.FILES)
        
        generic_file_output = request.FILES["generic_file"]
        print(generic_file_output)
        
        file_to_compare_output = request.FILES["file_to_compare"]
        print(file_to_compare_output)
        
        newfile = open("./media/final_result/final_"+str(generic_file_output), 'a')
        path = "./media/final_result/final_"+str(generic_file_output)
        newfile.write("-------------------------------------------------------------------\n")
        newfile.write("Differences noticed in File\n")
        newfile.write("-------------------------------------------------------------------\n")
        
        if form.is_valid():
            print("generic file")
            print(form)
            form.save()
            
            logger.info("Name of 1st file to be compared : {}".format(str(generic_file_output)))
            logger.info("Name of 1st file to be compared : {}".format(str(file_to_compare_output)))
            
            print("List ------->")
            
            file1 = open("./media/files/generic/"+str(generic_file_output), 'r')
            file2 = open("./media/files/file_to_compare/"+str(file_to_compare_output), 'r')

            Lines_of_file1 = file1.readlines()
            Lines_of_file2 = file2.readlines()

            file1_main = []
            file2_main = []

            logger.info("Comaparing files for any change detected")
            for lines in Lines_of_file1:
                file1_main.append(lines.replace("\n",''))

            for lines in Lines_of_file2:
                file2_main.append(lines.replace("\n",''))
                

            len_of_file1 = len(file1_main)
            len_of_file2 = len(file2_main)

            max_len = 0

            if len_of_file1 > len_of_file2:
                max_len = len_of_file1
            else:
                max_len = len_of_file2

            n,i,j=0,0,0


            output = []
            while(n<max_len):
                
                if i == len_of_file1:
                    newfile.write("Change occured in line no. {} -----> {}".format(j,file2_main[j]))
                    output.append("Change occured in line no. {} -----> {}\n".format(j,file2_main[j]))
                    j=j+1
                    n=n+1
                    
                elif j == len_of_file2:
                    print(file1_main[i])
                    i=i+1
                    n=n+1
                    
                else:
                    if file1_main[i] == file2_main[j]:
                        i=i+1
                        j=j+1
                        n=n+1
                    else:
                        output.append("Change occured in line no. {} -----> {}".format(j,file2_main[j]))
                        newfile.write("Change occured in line no. {} -----> {}\n".format(j,file2_main[j]))
                        j=j+1
                        n=n+1
            if len(output) == 0:
                output.append("No Changes detected")
            logger.info("Final path for saving the desired output of comparision ----->  ./media/final_result/final_"+str(generic_file_output))
        #    return redirect('list')
        return render(request, 'comapre_file.html',{
            'final_output': output,
            'path':path})
    else:
        form = CompareForm()
    
        
    return render(request, 'upload_file.html', {
        'form': form
    })


# def delete_book(request, pk):
#     if request.method == 'POST':
#         book = Book.objects.get(pk=pk)
#         book.delete()
#     return redirect('book_list')


# class BookListView(ListView):
#     model = Book
#     template_name = 'class_book_list.html'
#     context_object_name = 'books'


# class UploadBookView(CreateView):
#     model = Book
#     form_class = BookForm
#     success_url = reverse_lazy('class_book_list')
#     template_name = 'upload_book.html'
