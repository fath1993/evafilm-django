# Generated by Django 3.2.3 on 2021-06-17 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoEdit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titration_time', models.CharField(blank=True, default='0:0', max_length=55, null=True, verbose_name='تایم تیتر شروع اپیزود')),
                ('censor_times', models.TextField(blank=True, max_length=512, null=True, verbose_name='تایم سانسور')),
                ('episode', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Timing', to='movies.episode', verbose_name='اپیزود')),
            ],
        ),
        migrations.CreateModel(
            name='LikedPlayList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked', models.PositiveSmallIntegerField(choices=[(1, 'Like'), (0, 'Dislike')])),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.playlist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LikedPlaylist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HistoryPlayList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_time', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.episode')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HistoryPlaylist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Waiting for confirm'), (1, 'Confirmed')], default=0)),
                ('is_reveal', models.BooleanField(default=False)),
                ('date_shamsi', models.CharField(blank=True, max_length=25, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.playlist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookmarkPlayList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.playlist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BookmarkPlaylist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
