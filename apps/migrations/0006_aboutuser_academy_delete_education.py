# Generated by Django 4.1.4 on 2022-12-24 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_rename_school_education_academy'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutuser',
            name='academy',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Education',
        ),
    ]
