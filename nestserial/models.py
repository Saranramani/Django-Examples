from django.db import models

class Collage(models.Model):
    CType = models.CharField(max_length=50)

class Dept(models.Model):
    collage = models.ForeignKey(Collage,on_delete=models.CASCADE,related_name='collage')
    CollageCode = models.IntegerField()
    CollageName = models.CharField(max_length=50)
    CollageDistrict = models.CharField(max_length=50)
