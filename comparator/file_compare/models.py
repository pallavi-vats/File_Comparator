from django.db import models
from django.core.validators import FileExtensionValidator

class Compare(models.Model):
    generic_file = models.FileField(upload_to='files/generic/', verbose_name= "GENERIC FILE : ")
    file_to_compare = models.FileField(upload_to='files/file_to_compare/', verbose_name = "FILE TO COMPARE : ")

    def __str__(self):
        return str(self.generic_file)

    # def delete(self, *args, **kwargs):
    #     self.generic_file.delete()
    #     self.file_to_compare.delete()
    #     super().delete(*args, **kwargs)
    
class DoctoPdf(models.Model):
    word_file = models.FileField(upload_to='files/doc_file', verbose_name= "UPLOAD WORD FILE : ", validators=[FileExtensionValidator(allowed_extensions=["doc","docx"])])
   
    def __str__(self):
        return str(self.word_file)
    
class PdftoDoc(models.Model):
    pdf_file = models.FileField(upload_to='files/pdf_file', verbose_name= "UPLOAD PDF FILE : ", validators=[FileExtensionValidator(allowed_extensions=["pdf"])])
   
    def __str__(self):
        return str(self.pdf_file)
