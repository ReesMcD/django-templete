# Generated by Django 2.1.2 on 2018-11-26 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0035_auto_20181126_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='reoccuring',
            field=models.BooleanField(default=True),
        ),
    ]
