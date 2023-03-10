# Generated by Django 4.1.4 on 2022-12-24 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_experience_current'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='default.png', upload_to='services')),
            ],
        ),
    ]
