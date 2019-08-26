from django.contrib import admin
# . means current directory - so models file
from .models import Job

# Register your models here.

admin.site.register(Job)
