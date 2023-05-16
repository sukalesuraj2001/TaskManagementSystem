from django.contrib import admin
from mytask.models import MyTask

# Register your models here.
class MyTaskAdminClass(admin.ModelAdmin):
    list_display = ('task_title','desc','status')

admin.site.register(MyTask,MyTaskAdminClass)

