from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.



class MyTask(models.Model):
    
    task_title=models.CharField(max_length=50,verbose_name='task_title')
    desc=models.CharField(max_length=50,verbose_name='Description')
    sdate=models.DateField(default=timezone.now)
    edate=models.DateField(default=timezone.now)
    status = models.BooleanField(default=False,verbose_name='Status')


    def __str__(self):
        return self.task_title