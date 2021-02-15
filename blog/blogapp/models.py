from django.db import models
from django.utils import timezone
# Create your models here.

class Author(models.Model):
    author_name = models.CharField(max_length=164)
    author_surname = models.CharField(max_length=164)

    def __str__(self):
        return self.author_name + ' ' + self.author_surname

class Topic(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    topic_title = models.CharField(max_length=200)
    topic_description = models.CharField(max_length=300, default='No description')
    topic_text = models.TextField()
    pub_date = models.DateTimeField()
    topic_img = models.ImageField(upload_to='blogapp/blogimages', blank=True)

    def __str__(self):
        return self.topic_title + ' - by ' + str(self.author)
