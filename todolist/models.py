from django.db import models
import datetime

class TodoList(models.Model):
    title = models.CharField(max_length=250)
    created = models.DateField(default=datetime.date.today)
    
    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title