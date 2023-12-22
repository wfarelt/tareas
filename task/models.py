from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    limit_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
