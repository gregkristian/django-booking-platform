# Generated by Django 4.0.1 on 2022-10-20 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
    ]
