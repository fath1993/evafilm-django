# Generated by Django 3.2.3 on 2021-07-12 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftcard', '0014_alter_giftcard_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftcard',
            name='code',
            field=models.CharField(default='0a77cd62', max_length=255, unique=True, verbose_name='کد کارت هدیه'),
        ),
    ]
