# Generated by Django 4.0.4 on 2022-08-24 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_remove_signupmodel_upload_signupmodel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signupmodel',
            name='image',
        ),
    ]
