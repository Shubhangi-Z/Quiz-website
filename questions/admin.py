from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Domain)
admin.site.register(Course)
admin.site.register(Question)



