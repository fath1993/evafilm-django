# Generated by Django 3.2.3 on 2021-06-17 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_subscriptionplan_spacial_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionplan',
            name='spacial_id',
            field=models.CharField(default='048110e4', max_length=8),
        ),
    ]
