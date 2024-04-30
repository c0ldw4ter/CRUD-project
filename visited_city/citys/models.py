from django.db import models

class City(models.Model):
    
    city = models.CharField(max_length=100, verbose_name="Название города")
    date = models.DateField(verbose_name="Дата посещения")

    def __str__(self):
        return self.city