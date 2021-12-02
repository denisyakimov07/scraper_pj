from django.contrib import admin

# Register your models here.
from parser_pj.models import QSENews, QSENewsAR

class QSENewsAdmin(admin.ModelAdmin):
    list_display = ("company_title", "news_title", "news_body", "news_url", "news_date")

    def company_title(self, obj):
        return obj.company_title

    def news_title(self, obj):
        return obj.news_title

    def news_body(self, obj):
        return obj.news_body

    def news_download_attachment_url(self, obj):
        return obj.news_download_attachment_url

    def news_url(self, obj):
        return obj.news_urldef

    def news_date(self, obj):
        return obj.news_date

class QSENewsARAdmin(admin.ModelAdmin):
    list_display = ("company_title", "news_title", "news_body", "news_url", "news_date")

    def company_title(self, obj):
        return obj.company_title

    def news_title(self, obj):
        return obj.news_title

    def news_body(self, obj):
        return obj.news_body

    def news_download_attachment_url(self, obj):
        return obj.news_download_attachment_url

    def news_url(self, obj):
        return obj.news_urldef

    def news_date(self, obj):
        return obj.news_date



admin.site.register(QSENews, QSENewsAdmin)
admin.site.register(QSENewsAR, QSENewsARAdmin)