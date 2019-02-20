from django.contrib import admin

# Register your models here.
from .models import Userinfo
from .models import Usergroup

admin.site.register(Userinfo)
admin.site.register(Usergroup)