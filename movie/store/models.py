from django.db import models

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=50)
    year = models.IntegerField()
    image = models.ImageField(upload_to='store/img',null=True,blank=True)


    def __str__(self):
        return self.name



