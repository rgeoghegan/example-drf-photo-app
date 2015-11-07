from django.db import models

# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=200)
    photo = models.FileField(upload_to='photo_dir')
    user = models.ForeignKey('PhotoUser')
    viewers = models.ManyToManyField(
        'PhotoUser', related_name='can_view', blank=True
    )
    likes = models.IntegerField()

    def __str__(self):
        return self.title


class PhotoUser(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
