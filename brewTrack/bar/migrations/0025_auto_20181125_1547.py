# Generated by Django 2.1.2 on 2018-11-25 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0024_delete_drink'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='current_ammount',
            new_name='current_amount',
        ),
    ]