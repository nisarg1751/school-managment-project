from dataclasses import field, fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from student.models import SignUpModel,Marks

# choices for Userform
medium = [
    ('english','English'),
    ('gujrati','Gujrati')
]

# study = [
#     ('online','online'),
#     ('offline','offline')
# ]


# form for user registration
class SignUpForm(UserCreationForm):
    class Meta:   
        model = User
        fields = ['username','first_name','last_name','email']

# adding field in user registration form
class UserForm(forms.ModelForm):
    # medium = forms.CharField(max_length=270,label='Medium',widget=forms.RadioSelect(choices=medium))
    # study = forms.CharField(max_length=270,label='School Type',widget=forms.CheckboxSelectMultiple(choices=study))
    # online = forms.BooleanField()
    # offline = forms.BooleanField()
    # phone = forms.IntegerField()
    # image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    # video = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = SignUpModel
        fields = ['phone','medium','video','image']

# Edit profile form
class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class EditOtherDetailForm(forms.ModelForm):
    class Meta:
        model = SignUpModel
        fields = ['medium','study','phone','image','video']

class Marksform(forms.ModelForm):
    maths = forms.IntegerField()
    science = forms.IntegerField()
    hindi = forms.IntegerField()
    english = forms.IntegerField()
    class Meta:
        model = Marks
        fields = ['maths','science','hindi','english']

class MarksEditForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['maths','science','hindi','english']