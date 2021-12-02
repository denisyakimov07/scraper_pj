from django.contrib import admin

# Register your models here.
from parser_pj.models import QSENews, QSENewsAR

admin.site.register(QSENews)
admin.site.register(QSENewsAR)