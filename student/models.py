from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
# choices 
medium = [
    ('english','English'),
    ('gujrati','Gujrati')
]

# study = [
#     ('online','online'),
#     ('offline','offline')
# ]

# user registration model
class SignUpModel(models.Model):
    medium = models.CharField(max_length=270,choices=medium,null=True,blank=True)
    study = models.CharField(max_length=270,default="")
    # online = models.BooleanField(default=False)
    # offline = models.BooleanField(default=False)
    phone = models.IntegerField()
    image = models.ImageField(upload_to = 'media',default = 'media/ganpati.jpg')
    video = models.FileField(upload_to = 'video',default= ' ')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Marks(models.Model):
    maths = models.IntegerField()
    science = models.IntegerField()
    hindi = models.IntegerField()
    english = models.IntegerField()
    marks = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.marks)