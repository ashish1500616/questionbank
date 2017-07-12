from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils import timezone


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
    question_image1 = models.FileField(default=False, blank=True)
    question_image2 = models.FileField(default=False, blank=True)

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
    question_3_b = models.ImageField(blank=True) def approve_comment(self): return self.comments.filter(approve_comment=True) # def get_absolute_url(self): #     return reverse("question_paper", kwargs={'subid': self.subject_id}) 
    def __str__(self):
        return str(self.subject)


class College(models.Model):
    college_name = models.CharField(max_length=30)

    def __str__(self):
        return self.college_name


class Comment(models.Model):
    subject = models.ForeignKey('Subject', related_name='comments', default="")
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

