# Generated by Django 4.0.1 on 2022-10-13 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookableobject',
            old_name='user',
            new_name='owner',
        ),
    ]