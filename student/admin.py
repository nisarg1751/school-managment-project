from django.contrib import admin
from student import models
from student.models import SignUpModel,Marks
# # Register your models here.


# register model for signup
admin.site.register(SignUpModel)
admin.site.register(Marks)
