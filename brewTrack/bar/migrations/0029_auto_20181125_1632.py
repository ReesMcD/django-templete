# Generated by Django 2.1.2 on 2018-11-25 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0028_auto_20181125_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='location',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='subtype',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.CharField(default='', max_length=20),
        ),
    ]