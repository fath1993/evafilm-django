# Generated by Django 3.2.3 on 2021-09-28 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftcard', '0027_alter_giftcard_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftcard',
            name='code',
            field=models.CharField(default='16c5dbe0', max_length=255, unique=True, verbose_name='کد کارت هدیه'),
        ),
    ]
