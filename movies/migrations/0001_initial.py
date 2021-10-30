# Generated by Django 3.2.3 on 2021-06-17 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import movies.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35, verbose_name='نام بازیگر')),
                ('summary', models.TextField(max_length=1024, verbose_name='درباره بازیگر')),
                ('thumb_image', models.ImageField(blank=True, null=True, upload_to=movies.models.image_path, verbose_name='تصویر بازیگر')),
                ('page_url', models.CharField(blank=True, help_text='This field is Read Only', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveSmallIntegerField(default=1)),
                ('name_en', models.CharField(max_length=35, unique=True)),
                ('name_fa', models.CharField(max_length=35)),
                ('page_url', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('mobile_or_email', models.CharField(max_length=80)),
                ('message', models.TextField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35, unique=True)),
                ('page_url', models.CharField(blank=True, help_text='This field is Read Only', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35, verbose_name='نام کارگردان')),
                ('summary', models.TextField(max_length=1024, verbose_name='درباره کارگردان')),
                ('thumb_image', models.ImageField(blank=True, null=True, upload_to=movies.models.image_path, verbose_name='تصویر کارگردان')),
                ('page_url', models.CharField(blank=True, help_text='This field is Read Only', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'فیلم'), (2, 'سریال')], default=1, verbose_name='نوع فیلم')),
                ('name_en', models.CharField(max_length=55, verbose_name='نام انگلیسی')),
                ('name_fa', models.CharField(max_length=55, verbose_name='نام فارسی')),
                ('summary', models.TextField(max_length=1024, verbose_name='خلاصه فیلم')),
                ('imdb_score', models.FloatField(default=0, verbose_name='IMDB امتیاز')),
                ('users_score', models.FloatField(default=0, verbose_name='امتیاز کاربران')),
                ('publish_status', models.CharField(blank=True, max_length=55, null=True)),
                ('is_free', models.BooleanField(default=False, verbose_name='رایگان است')),
                ('visit_times', models.IntegerField(default=0)),
                ('play_times', models.IntegerField(default=0)),
                ('year', models.CharField(max_length=4, verbose_name='سال')),
                ('time', models.CharField(max_length=55, verbose_name='مدت زمان فیلم')),
                ('tv_pg', models.PositiveSmallIntegerField(choices=[(1, 'زیر سه سال'), (3, '3 تا 6 سال'), (7, '7 تا 12 سال'), (13, 'مناسب برای بالای 13 سال'), (17, 'مناسب برای بالای 17 سال')], default=5, verbose_name='درجه بندی سنی')),
                ('thumb_image', models.ImageField(blank=True, null=True, upload_to=movies.models.image_path, verbose_name='تصویر فیلم')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('users_score_n', models.IntegerField(default=0)),
                ('users_score_p', models.IntegerField(default=0)),
                ('trailer_url', models.CharField(blank=True, max_length=512, null=True, verbose_name='آدرس تریلر')),
                ('page_url', models.CharField(blank=True, help_text='This field is Read Only', max_length=255, null=True)),
                ('actor', models.ManyToManyField(blank=True, to='movies.Actor', verbose_name='بازیگران')),
                ('category', models.ManyToManyField(related_name='Playlists', to='movies.Category', verbose_name='دسته بندی و ژانر')),
                ('country', models.ManyToManyField(to='movies.Country', verbose_name='کشور')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('director', models.ManyToManyField(blank=True, to='movies.Director', verbose_name='کارگردان')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.PositiveSmallIntegerField(choices=[(0, 'انتخاب نشده'), (1, 'فصل 1'), (2, 'فصل 2'), (3, 'فصل 3'), (4, 'فصل 4'), (5, 'فصل 5'), (6, 'فصل 6'), (7, 'فصل 7'), (8, 'فصل 8'), (9, 'فصل 9'), (10, 'فصل 10'), (11, 'فصل 11'), (12, 'فصل 12')], default=0, verbose_name='نام/شماره فصل')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Seasons', to='movies.playlist', verbose_name='فیلم/سریال')),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=55, null=True)),
                ('index', models.PositiveSmallIntegerField(default=1, verbose_name='اپیزود')),
                ('summary', models.TextField(blank=True, max_length=512, null=True, verbose_name='خلاصه این اپیزود')),
                ('is_available_in_720p', models.BooleanField(default=True, verbose_name='در دسترس با کیفیت 720p')),
                ('is_available_in_1080p', models.BooleanField(default=False, verbose_name='در دسترس با کیفیت 1080p')),
                ('thumb_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='تصویر انگشتی')),
                ('stream_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='لینک پخش ')),
                ('download_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='لینک دانلود')),
                ('subtitle_vtt_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='زیرنویس VTT')),
                ('subtitle_srt_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='زیرنویس SRT')),
                ('page_url', models.CharField(blank=True, help_text='This field is Read Only', max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Episodes', to='movies.playlist', verbose_name='فیلم/سریال')),
                ('season', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Episodes', to='movies.season', verbose_name='فصل')),
            ],
        ),
    ]
