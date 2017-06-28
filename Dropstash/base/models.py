from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='user', on_delete=models.CASCADE, primary_key=True)
    avatar = models.ImageField(verbose_name='avatar')
    # Description?
    # PageReferences?
    # Saved quotes?


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
#     message = models.TextField(verbose_name='author comment')
#     submission_datetime = models.DateTimeField(verbose_name='submission datetime', default=datetime.now, blank=True)
#     is_published = models.BooleanField(default=False, blank=True, verbose_name='publication marker')
#
#     # invalid logic
#     publication_datetime = models.DateTimeField(verbose_name='publication datetime', default=datetime.now, blank=True)


# class PostComment(models.Model):
#     post = models.ForeignKey(Post, verbose_name='post', on_delete=models.CASCADE)


# class Repost(models.Model):
#     author = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, verbose_name='post', on_delete=models.CASCADE)
#     publication_datetime = models.DateTimeField(verbose_name='publication datetime', default=datetime.now, blank=True)


# class PageReference(models.Model):
#     title = models.CharField(max_length=200, verbose_name='title')
#     description = models.TextField(verbose_name='description')
#     picture = models.ImageField(verbose_name='picture')
#     author = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE)
#     # Posts and reposts?
#     submission_datetime = models.DateTimeField(verbose_name='submission datetime', default=datetime.now, blank=True)

#
# class Collection(models.Model):
#     pass
#     # PageReference? layout?

