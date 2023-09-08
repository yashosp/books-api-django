from django.db import models

# Create your models here.
# models translate python code to SQL(database code)

class Book(models.Model):
    title = models.CharField(max_length=100) # string field,
    number_of_pages = models.IntegerField()
    publish_date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.title