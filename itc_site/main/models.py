from django.db import models


class Task(models.Model):
    title = models.CharField('Text', max_length=50)
    task = models.TextField('Description')

    def __str__(self):
        return self.title

