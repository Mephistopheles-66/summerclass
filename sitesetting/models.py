from django.db import models

# Create your models here.

class SiteSetting(models.Model):
    site_title = models.CharField(max_length=200, default="MarketPlace")
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=200, blank=True, null=True)
    logo = models.ImageField(upload_to="photos/logos/", blank=True, null=True)
    favicon = models.ImageField(upload_to="photos/favicons/", blank=True, null=True)

    def __str__(self):
        return "Site Setting"


    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"

