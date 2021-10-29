from datetime import datetime
from django.db import models

class Paste(models.Model):
    author = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True, unique=True)
    date = models.DateTimeField(default=datetime.now, blank=False)
    external_id  = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        str = self.title
        if not str:
            str = self.author
        return str