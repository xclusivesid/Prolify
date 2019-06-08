# Generated by Django 2.0.7 on 2019-05-20 21:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('album', '0011_auto_20181002_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=250)),
                ('last_name', models.CharField(default='', max_length=250)),
                ('country', models.CharField(max_length=250)),
                ('location', models.CharField(default='Abia,Nigeria', max_length=250)),
                ('description', models.TextField()),
                ('phone_number', models.CharField(blank=True, default='+234', max_length=14, null=True)),
                ('photo', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]