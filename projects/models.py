from django.db import models

# Create your models here.
class Task(models.Model):
    sl_no= models.IntegerField(max_length=250)
    item_name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.sl_no
