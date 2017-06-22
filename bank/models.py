from django.db import models
from django.core.urlresolvers import reverse

class Album(models.Model):
    subject = models.CharField(max_length=250,default=False)
    semester = models.CharField(max_length=250)
    branch = models.CharField(max_length=500)
    concatenate = models.CharField(max_length=100)
    upload_paper = models.FileField(default=False)
    a = models.FileField(default=False)

    def get_absolute_url(self):
       return reverse('bank:detail', kwargs={'pk': self.pk})

    def __str__(self):
         return self.subject

class Song(models.Model):
    subject = models.ForeignKey(Album, on_delete=models.CASCADE)
    semester = models.CharField(max_length=10)
    year = models.CharField(max_length=250)
    upload_solutions = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def get_absolute_url(self):
       return reverse('bank:home',)


    def __str__(self):
        return self.year


class Test(models.Model):
    subject = models.CharField(max_length=250,default=False)
    semester = models.CharField(max_length=250)
    branch = models.CharField(max_length=500)
    concatenate = models.CharField(max_length=100)
    upload_paper = models.FileField(default=False)
    a = models.FileField(default=False)

    def get_absolute_url(self):
       return reverse('bank:detail', kwargs={'pk': self.pk})

    def __str__(self):
         return self.subject