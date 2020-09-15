from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class MusicWork(models.Model):
    iswc = models.CharField('ISWC', max_length=30, null=True, default=None)
    title = models.CharField(max_length=128, null=True, default=None)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title
