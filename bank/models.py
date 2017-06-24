from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings


class Album(models.Model):
    subject = models.CharField(max_length=250, default=False)
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
    subject = models.CharField(max_length=250, default=False)
    semester = models.CharField(max_length=250)
    branch = models.CharField(max_length=500)
    concatenate = models.CharField(max_length=100)
    upload_paper = models.FileField(default=False)
    a = models.FileField(default=False)

    def get_absolute_url(self):
        return reverse('bank:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.branch


class Branch(models.Model):
    branch_name = models.CharField(max_length=30)
    branch_image = models.FileField(default=False, blank=True)

    def __str__(self):
        return self.branch_name


class Semester(models.Model):
    semester_name = models.CharField(max_length=30)

    def __str__(self):
        return self.semester_name


class Subject(models.Model):
    semester = models.ForeignKey('Semester', on_delete=models.CASCADE, default=True)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE, default=True)
    subject_name = models.CharField(max_length=30)
    subject_image = models.FileField(default=False, blank=True)
    question_image = models.FileField(default=False, blank=True)

    def __str__(self):
        return self.subject_name
