from django.db import models

# Create your models here.
class Hero(models.Model):
    status=models.CharField(max_length=100)
    win_score=models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)
