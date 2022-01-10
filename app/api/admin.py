from django.contrib import admin

# Register your models here.
from api.models.course import Course

admin.site.register(Course)