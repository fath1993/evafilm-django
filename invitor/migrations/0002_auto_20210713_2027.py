# Generated by Django 3.2.3 on 2021-07-13 15:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('invitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generated_invitor_code',
            name='code',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='generated_invitor_code',
            name='invited_users',
            field=models.ManyToManyField(blank=True, related_name='invited_users_g', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='invitor_code',
            name='invited_users',
            field=models.ManyToManyField(blank=True, related_name='invited_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
