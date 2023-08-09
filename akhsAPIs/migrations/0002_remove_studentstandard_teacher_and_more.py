# Generated by Django 4.2.4 on 2023-08-08 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akhsAPIs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentstandard',
            name='teacher',
        ),
        migrations.AddField(
            model_name='studentstandard',
            name='teacher',
            field=models.ManyToManyField(related_name='standards', to='akhsAPIs.teacher'),
        ),
    ]
