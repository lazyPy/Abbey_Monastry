from django.db import models



class Brother(models.Model):

    name = models.CharField(max_length=100, verbose_name="Brother's Name")
    age = models.FloatField(null=True, verbose_name="Brother's Age (optional)")
    about = models.TextField(verbose_name='About Brother (optional)', null=True)
    img = models.ImageField(verbose_name="Brother's Image", null=False, upload_to='brothers')

    def __str__(self):

        return self.name 
    


    

