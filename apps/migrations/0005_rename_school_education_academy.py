# Generated by Django 4.1.4 on 2022-12-24 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_aboutuser_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='school',
            new_name='academy',
        ),
    ]
