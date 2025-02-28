from django.urls import path, include

from . import views
#from .views import file_list, upload_file

urlpatterns = [
    ##################################
    # --------------Home Page---------
    ##################################
    path('', views.home, name='home'),
    path('list', views.file_list, name='list'),
    path('upload', views.upload_file, name='upload'),
    path('doc2pdf', views.word_to_pdf, name="doc2pdf"),
    path('pdf2doc', views.pdf_to_word, name="pdf2doc"),
    path('file_selector', views.file_selector, name="file_selector"),
]