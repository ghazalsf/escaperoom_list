from django.db import models

# Create your models here.

class escaperoom(models.Model):

    escaperoom_name = models.CharField(max_length=1000)

    def __str__(self):
        return self.escaperoom_name

