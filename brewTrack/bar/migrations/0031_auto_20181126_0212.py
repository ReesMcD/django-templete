# Generated by Django 2.1.2 on 2018-11-26 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0030_auto_20181125_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='frequancy',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Frequancy'),
        ),
        migrations.AlterField(
            model_name='bar',
            name='hours',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='bar',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.CharField(default='', max_length=20, verbose_name='Event Date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(default='None Menu', max_length=20),
        ),
    ]