from django.contrib import admin
from .models import Branch, Semester, Subject, College, Question, Comment

# admin.site.register(Album)
# admin.site.register(Song)
# admin.site.register(Test)
admin.site.register(College)
admin.site.register(Semester)
admin.site.register(Branch)
admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(Comment)
