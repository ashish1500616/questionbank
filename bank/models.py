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
    question_1_a = models.ImageField(blank=True)
    question_1_b = models.ImageField(blank=True)
    question_two_a = models.ImageField(blank=True)
    question_two_b = models.ImageField(blank=True)
    question_3_a = models.ImageField(blank=True)
    question_3_b = models.ImageField(blank=True)

    def __str__(self):
        return str(self.subject)


class College(models.Model):
    college_name = models.CharField(max_length=30)

    def __str__(self):
        return self.college_name
