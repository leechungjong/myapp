from django.db import models
from django.utils import timezone
from django.db.models import F

class Board(models.Model):
    title = models.CharField(max_length=30, unique=True)
    writer = models.CharField(max_length=20)
    content = models.TextField()  # max_length 제거
    created_at = models.DateTimeField(default=timezone.now)
    read_count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}. {self.writer}({self.read_count})'

    def increase_read_count(self):
        self.read_count = F('read_count') + 1
        self.save(update_fields=['read_count'])
        self.refresh_from_db(fields=['read_count'])
