from django.db import models

# Create your models here.
from django.utils import timezone

class Board(models.Model):
    title = models.CharField(max_length=30, unique=True)
    writer = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    read_count = models.IntegerField(default=0)

    def __str__(self):
        return '%s. %s(%d)' % (self.title, self.writer, self.read_count)
    def increase_read_count(self):
        self.read_count += 1
        self.save()
        