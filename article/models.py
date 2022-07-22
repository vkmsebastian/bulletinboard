from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    pub_date = models.DateTimeField()
