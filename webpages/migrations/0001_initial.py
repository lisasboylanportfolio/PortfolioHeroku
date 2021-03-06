# Generated by Django 2.2 on 2019-04-18 04:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('desc', models.TextField(max_length=200)),
                ('link', models.TextField(blank=True, validators=[django.core.validators.URLValidator()])),
                ('image', models.FileField(blank=True, null=True, upload_to='project_images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
