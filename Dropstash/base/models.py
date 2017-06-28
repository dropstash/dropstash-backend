from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='user', on_delete=models.CASCADE, primary_key=True)
    avatar = models.ImageField(verbose_name='avatar')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# class Hyperlink(models.Model):
#     target_url = models.URLField(max_length=200, verbose_name='hyperlink')
#     comment = models.TextField(verbose_name='comment')
#     picture = models.ImageField(verbose_name='picture')


# class Post(models.Model):
#     author = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE)
#     collection = models.ForeignKey(Collection, verbose_name='collection', on_delete=models.CASCADE)
#     link = models.ForeignKey(Hyperlink, verbose_name='hyperlink', on_delete=models.CASCADE)
#     is_published = models.BooleanField(default=False, blank=True, verbose_name='publication marker')
#     publication_datetime = models.DateTimeField(verbose_name='publication date', default=datetime.now, blank=True)


# class PostComment(models.Model):
#     post = models.ForeignKey(Post, verbose_name='post', on_delete=models.CASCADE)

#
# class Collection(models.Model):
#     pass

