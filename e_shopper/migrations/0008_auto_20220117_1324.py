# Generated by Django 3.2.3 on 2022-01-17 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('e_shopper', '0007_auto_20220112_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='address',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='image',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='zip',
        ),
        migrations.AddField(
            model_name='userdetails',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='UpdateProfileImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(default='4568172.jpg', upload_to='media')),
                ('bio', models.CharField(max_length=250, null=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('mobile_no', models.CharField(max_length=13, null=True)),
                ('zipcode', models.CharField(max_length=6, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
