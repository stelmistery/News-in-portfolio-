from django.db import models


class Main(models.Model):
    name = models.TextField()
    about = models.TextField()
    fb = models.TextField(default='-')
    tw = models.TextField(default='-')
    yt = models.TextField(default='-')