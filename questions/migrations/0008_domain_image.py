# Generated by Django 3.2 on 2021-04-13 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
