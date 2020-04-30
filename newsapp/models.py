from django.db import models
from PIL import Image


class Article(models.Model):
    name = models.CharField(max_length=50)
    short_txt = models.TextField()
    body_txt = models.TextField()
    date = models.CharField(max_length=12)
    picurl = models.TextField(default='-')
    picname = models.TextField()
    writer = models.CharField(max_length=50)
    catname = models.CharField(max_length=50, default="-")
    catid = models.IntegerField(default=0)
    show = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    #
    # def save(self):
    #     super().save()
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)