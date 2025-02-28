# Generated by Django 4.1.3 on 2022-11-10 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_compare', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compare',
            name='file_to_compare',
            field=models.FileField(upload_to='files/file_to_compare/', verbose_name='FILE TO COMPARE : '),
        ),
        migrations.AlterField(
            model_name='compare',
            name='generic_file',
            field=models.FileField(upload_to='files/generic/', verbose_name='GENERIC FILE : '),
        ),
    ]
