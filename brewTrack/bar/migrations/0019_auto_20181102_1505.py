# Generated by Django 2.1.1 on 2018-11-02 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0018_auto_20181102_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='bar',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]