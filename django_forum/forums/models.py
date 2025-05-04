from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Categories'

class GlobalCounter(models.Model):
    counter = models.PositiveIntegerField(default=0)

    @classmethod
    def get_next(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        obj.counter += 1
        obj.save()
        return obj.counter

class Forum(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='forums')
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='forum_images/', blank=True, null=True)
    global_id = models.PositiveIntegerField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    global_id = models.PositiveIntegerField(unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.content[:30]}"

class Moderator(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128) 

    def __str__(self):
        return self.username

class Ad(models.Model):
    image = models.ImageField(upload_to='ads/')
    link = models.URLField()

    def __str__(self):
        return self.link