import django
from django.db import models
from django.utils import timezone


class QSENews(models.Model):
    company_title = models.CharField(max_length=600, null=False, blank=True)
    news_title = models.TextField(null=False, blank=True)
    news_body = models.TextField(null=False, blank=True)
    news_date = models.DateTimeField(null=True, blank=True)
    news_download_attachment_url = models.TextField(null=True, blank=True)
    news_url = models.TextField(null=False, blank=True)
    creat = models.DateTimeField(null=True, blank=True, default=django.utils.timezone.now)


    def __str__(self):
        return f"{self.company_title} - {self.news_title} - {self.news_date}"


class QSENewsAR(models.Model):
    company_title = models.CharField(max_length=600, null=False, blank=True)
    news_title = models.TextField(null=False, blank=True)
    news_body = models.TextField(null=False, blank=True)
    news_date = models.DateTimeField(null=True, blank=True)
    news_download_attachment_url = models.TextField(null=True, blank=True)
    news_url = models.TextField(null=False, blank=True)
    creat = models.DateTimeField(null=True, blank=True, default=django.utils.timezone.now)


    def __str__(self):
        return f"{self.company_title} - {self.news_title} - {self.news_date}"