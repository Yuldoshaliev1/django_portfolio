# Generated by Django 4.1.4 on 2022-12-25 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0009_education_college'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='current',
            field=models.CharField(max_length=60),
        ),
    ]
