# Generated by Django 2.0.4 on 2018-04-22 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblogspot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
