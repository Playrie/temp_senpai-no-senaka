# Generated by Django 3.2.3 on 2021-07-10 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210710_1851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restrequest',
            old_name='start_date',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='restrequest',
            name='end_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='終了日時'),
        ),
        migrations.AlterField(
            model_name='restrequest',
            name='start_time',
            field=models.TimeField(blank=True, null=True, verbose_name='時間'),
        ),
    ]
