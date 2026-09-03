from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    favorites = models.ManyToManyField('recipes.Recipe', related_name='favorited_by', blank=True)

    def __str__(self):
        return self.user.username
