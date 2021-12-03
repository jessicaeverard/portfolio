from django.db import models

# Create your models here.
class Job(models.Model):
    #images
    image = models.ImageField(upload_to='images/') #data saved as image format i/e jpeng, png
    #summary
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary
