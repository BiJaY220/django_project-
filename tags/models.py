from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
class Tag(models.Model):
    label = models.CharField(max_lenght =255 )

class tag_item(models.Model):
    tag = models.ForeignKey(Tag, on_delete= models.CASCADE )
    #type(product,video,article
    # #ID)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) #contenttype abstract type comes with django 
    object_type = models.PositiveIntegerField()
    content_object = models.GenericforeignKey()
    




# Create your models here.
