from django.db import models

# Create your models here.
class RestRequest(models.Model):
    kerbero_id = models.IntegerField(verbose_name="個体ID")
    head_name = models.CharField(max_length=255, verbose_name="頭の名前")
    requested = models.BooleanField(default=False)
    date = models.DateField(verbose_name="日付")
    start_time = models.TimeField(blank = True,null = True,verbose_name="時間")
    end_datetime = models.DateTimeField(blank = True,null = True,verbose_name="終了日時")

class Schedule(models.Model):
    kerbero_id = models.IntegerField(verbose_name="個体ID")
    date = models.DateField(verbose_name="日付")
    left_head_name = models.CharField(max_length=255, verbose_name="一つ目の頭の名前")
    left_start_time = models.CharField(max_length=255, verbose_name="一つ目の開始時刻")
    left_end_time = models.CharField(max_length=255, verbose_name="一つ目の終了時刻")
    center_head_name = models.CharField(max_length=255, verbose_name="二つ目の頭の名前")
    center_start_time = models.CharField(max_length=255, verbose_name="二つ目の開始時刻")
    center_end_time = models.CharField(max_length=255, verbose_name="二つ目の終了時刻")
    right_head_name = models.CharField(max_length=255, verbose_name="三つ目の頭の名前")
    right_start_time = models.CharField(max_length=255, verbose_name="三つ目の開始時刻")
    right_end_time = models.CharField(max_length=255, verbose_name="三つ目の終了時刻")