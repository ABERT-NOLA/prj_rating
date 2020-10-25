from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    desc = models.TextField()
    image_url = models.ImageField(default='default.jpg', upload_to='project_pics')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tech_used = models.CharField(max_length=250)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk}) 


    @classmethod
    def get_all_posts(cls):
        return cls.objects.order_by('-date_posted')

class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.content