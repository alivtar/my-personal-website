from django.db import models

# Create your models here.

class Blogs(models.Model):
    title = models.CharField(max_length = 100)
    publication_date = models.DateTimeField(auto_now = False, auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True, auto_now_add = False)
    text = models.TextField()
    image = models.ImageField(upload_to = 'images/')
