# Generated by Django 4.0.4 on 2022-08-24 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_remove_signupmodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='signupmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
    ]
