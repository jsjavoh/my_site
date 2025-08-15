from django.db import models


class Project(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    # image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name
