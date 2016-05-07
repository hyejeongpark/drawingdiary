from django.db import models


class Diary(models.Model):
    drawing = models.ImageField()
    date = models.DateField()
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
