from django.db import models


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField(max_length=50)
    lte_exists = models.BooleanField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True)


    def __str__(self):
        return f'{self.id}, {self.name}'


