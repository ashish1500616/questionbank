from django.db import models

# Create your models here.


class Iitppaper(models.Model):
    subject = models.CharField(max_length=250,default=False)
    semester = models.CharField(max_length=250)
    branch = models.CharField(max_length=500)
    concatenate = models.CharField(max_length=100)
    upload_paper = models.FileField(default=False)


class Iitpsoln(models.Model):
    subject = models.ForeignKey(Iitppaper, on_delete=models.CASCADE)
    semester = models.CharField(max_length=10)
    year = models.CharField(max_length=250)
    upload_solutions = models.FileField()
    is_favorite = models.BooleanField(default=False)

