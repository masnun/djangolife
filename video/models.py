from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField("Title", max_length=250)
    embed_code = models.TextField("Embed Code")

    def __str__(self):
        return self.title
