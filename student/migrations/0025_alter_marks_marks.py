# Generated by Django 4.0.4 on 2022-08-26 04:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0024_alter_signupmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='marks',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
