from django.contrib import admin
from RegApp.models import StudentModel


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', 'message')


admin.site.register(StudentModel, StudentAdmin)
