from django.contrib import admin

# from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from .models import Rubric, Article

# Register your models here.
# admin.site.register(Rubric)
# admin.site.register(Rubric, MPTTModelAdmin)
admin.site.register(Rubric, DraggableMPTTAdmin)
admin.site.register(Article)
