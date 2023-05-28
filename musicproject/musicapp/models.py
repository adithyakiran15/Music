from django.db import models

# Create your models here.
class Music(models.Model):
    name=models.CharField(max_length=250)
    singer=models.TextField()
    tag=models.TextField()
    img=models.ImageField(upload_to='gallary')
    file=models.FileField(upload_to='image')

    def __str__(self):
        return self.name