# Generated by Django 3.2.3 on 2021-08-12 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftcard', '0021_alter_giftcard_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftcard',
            name='code',
            field=models.CharField(default='3692ff0f', max_length=255, unique=True, verbose_name='کد کارت هدیه'),
        ),
    ]
