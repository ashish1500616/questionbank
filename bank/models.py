from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.conf import settings


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
    college= models.ForeignKey('College', on_delete=models.CASCADE, default=True)
    semester = models.ForeignKey('Semester', on_delete=models.CASCADE, default=True)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE, default=True)
    subject_name = models.CharField(max_length=30)
    subject_image = models.FileField(default=False, blank=True)
    question_image1 = models.FileField(default=False, blank=True)
    question_image2 = models.FileField(default=False, blank=True)

    def __str__(self):
        return self.subject_name


class College(models.Model):
    college_name=models.CharField(max_length=30)

    def __str__(self):
        return self.college_name


class Comments(models.Model):
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, default=True)
    name = models.CharField(max_length=20)
    body = models.TextField(max_length=1000)
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
