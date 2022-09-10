from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(blank=False,default=False,null=False)
    slug = models.SlugField(null=True,blank=True)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "My Blog"
        verbose_name_plural = "My Blogs"
    
