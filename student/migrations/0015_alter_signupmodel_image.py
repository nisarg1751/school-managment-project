# Generated by Django 4.0.4 on 2022-08-25 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_alter_signupmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupmodel',
            name='image',
            field=models.ImageField(default='media/ganpati.jpg', upload_to='media'),
        ),
    ]
