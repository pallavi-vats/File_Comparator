from django.contrib import admin
from .models import Compare, DoctoPdf, PdftoDoc

# Register your models here.
admin.site.register(Compare)
admin.site.register(DoctoPdf)
admin.site.register(PdftoDoc)