from django.db import models

from apps.common.fileUpload.userPath import userDirectoryPath


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Başlık')
    author = models.CharField(max_length=100, verbose_name='Yazar')
    image = models.ImageField(upload_to=userDirectoryPath, null=True, verbose_name='Kapak Resmi', blank=True)
    publication_date = models.CharField(max_length=100, verbose_name='Yayın Tarihi')

    def __str__(self):
        return self.title
