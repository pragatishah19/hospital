from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Docs(models.Model):
    name = models.CharField(max_length=32)
    emailid = models.EmailField(max_length=20)
    mobile=models.IntegerField()
    address=models.CharField(max_length=50)
    pic = models.ImageField(upload_to = 'doc_pic',null = True,blank = True)

    def __str__(self):
        return self.name

