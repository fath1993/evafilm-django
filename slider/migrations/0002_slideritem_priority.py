# Generated by Django 3.2.3 on 2021-09-30 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideritem',
            name='priority',
            field=models.PositiveIntegerField(default=0, verbose_name='الویت'),
        ),
    ]
