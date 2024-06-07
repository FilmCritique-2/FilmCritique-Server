from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=200)
    rating = models.FloatField()
    review = models.TextField()
    date_watched = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=6)
    poster = models.ImageField(blank=True, upload_to='poster_images/')

    def __str__(self):
        return self.title