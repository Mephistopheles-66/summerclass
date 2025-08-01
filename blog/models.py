from django.db import models
from django.utils import timezone

class blogcategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
# Create your models here.

class blog(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=0)
    category = models.ForeignKey(blogcategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name