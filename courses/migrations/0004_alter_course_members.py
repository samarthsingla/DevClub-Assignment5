# Generated by Django 4.0.6 on 2022-08-01 18:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0003_alter_course_code_alter_course_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='members',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL, verbose_name='Students'),
        ),
    ]
