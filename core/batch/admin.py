from django.contrib import admin

# Register your models here.
from .models import Enroll,Category

admin.site.register(Enroll)
admin.site.register(Category)