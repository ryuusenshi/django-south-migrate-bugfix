from django.db import models
# Create your models here.

class MyModel(models.Model):
    my_field1 = models.BooleanField(default=True)
    my_field2 = models.BooleanField(default=False)
