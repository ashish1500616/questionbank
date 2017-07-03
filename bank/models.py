from django.db import models
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
    college = models.ForeignKey('College', on_delete=models.CASCADE, default=True)
    semester = models.ForeignKey('Semester', on_delete=models.CASCADE, default=True)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE, default=True)
    subject_name = models.CharField(max_length=30)
    subject_image = models.FileField(default=False, blank=True)
    question_image = models.FileField(default=False, blank=True)

    def __str__(self):
        return self.subject_name


class Question(models.Model):
    college = models.ForeignKey('College', on_delete=models.CASCADE, default=True)
    semester = models.ForeignKey('Semester', on_delete=models.CASCADE, default=True)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE, default=True)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, default=True)
    question1 = models.FileField(default=False, blank=True, editable=True)
    question2 = models.FileField(default=False, blank=True, editable=True)

    def __str__(self):
        return str(self.subject)


class College(models.Model):
    college_name = models.CharField(max_length=30)

    def __str__(self):
        return self.college_name
