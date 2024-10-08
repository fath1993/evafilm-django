# Generated by Django 3.2.1 on 2021-05-08 07:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('title', models.CharField(max_length=55)),
                ('valid_days', models.PositiveSmallIntegerField()),
                ('price', models.IntegerField()),
                ('is_vip', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(blank=True, max_length=12, null=True)),
                ('age', models.PositiveSmallIntegerField(blank=True, default=28, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_subscribed', models.BooleanField(default=False)),
                ('api_token', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateField()),
                ('last_login', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('ip_1', models.CharField(blank=True, max_length=15, null=True)),
                ('ip_2', models.CharField(blank=True, max_length=15, null=True)),
                ('ip_3', models.CharField(blank=True, max_length=15, null=True)),
                ('plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.subscriptionplan')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='SubscriptionPlan', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
