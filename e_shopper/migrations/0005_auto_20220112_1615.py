# Generated by Django 3.2.3 on 2022-01-12 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_shopper', '0004_auto_20220112_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='last_name',
        ),
    ]
