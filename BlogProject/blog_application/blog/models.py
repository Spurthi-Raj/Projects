from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify



# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200,unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='posts')
    is_published = models.BooleanField(default=False)
    slug = models.SlugField(blank=True,null=True) 

    def __str__(self):
        return self.title


    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    class Meta:
        ordering = ['-created_at']


    