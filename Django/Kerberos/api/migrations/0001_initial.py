# Generated by Django 3.2.3 on 2021-07-10 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RestRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kerbero_id', models.IntegerField(max_length=255, verbose_name='個体ID')),
                ('head_name', models.CharField(max_length=255, verbose_name='頭の名前')),
                ('requested', models.BooleanField(default=False)),
                ('start_date', models.DateField(verbose_name='日付')),
                ('start_time', models.TimeField(verbose_name='時間')),
                ('end_datetime', models.DateTimeField(verbose_name='終了日時')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kerbero_id', models.IntegerField(max_length=255, verbose_name='個体ID')),
                ('date', models.DateField(verbose_name='日付')),
                ('first_head_name', models.CharField(max_length=255, verbose_name='一つ目の頭の名前')),
                ('first_start_time', models.CharField(max_length=255, verbose_name='一つ目の開始時刻')),
                ('first_end_time', models.CharField(max_length=255, verbose_name='一つ目の終了時刻')),
                ('second_head_name', models.CharField(max_length=255, verbose_name='二つ目の頭の名前')),
                ('second_start_time', models.CharField(max_length=255, verbose_name='二つ目の開始時刻')),
                ('second_end_time', models.CharField(max_length=255, verbose_name='二つ目の終了時刻')),
                ('third_head_name', models.CharField(max_length=255, verbose_name='三つ目の頭の名前')),
                ('third_start_time', models.CharField(max_length=255, verbose_name='三つ目の開始時刻')),
                ('third_end_time', models.CharField(max_length=255, verbose_name='三つ目の終了時刻')),
            ],
        ),
    ]
