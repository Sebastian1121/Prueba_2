from django.db import models

# Create your models here.
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances



# Create your models here.


class Genre(models.Model):
    #Model representing a book genre."""
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name


class Juego(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=200)
    genre = models.ManyToManyField(Genre)
    summary = models.TextField(max_length=1000)
    url = models.URLField(max_length=100, default='')
    image = models.ImageField(upload_to='images/', null=True, blank=True)



    class Meta:
        ordering=['title']

    def str(self):
        #return f'{self.id} ({self.title})'
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('movie-detail', args=[str(self.id)])