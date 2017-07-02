from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail

from datetime import datetime

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name='username', max_length=20)
    email = models.EmailField(verbose_name='email address', unique=True)
    first_name = models.CharField(verbose_name='first name', max_length=20, blank=True)
    last_name = models.CharField(verbose_name='last name', max_length=20, blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='active status', default=True)
    is_staff = models.BooleanField(verbose_name='staff status', default=False)

    avatar = models.ImageField(verbose_name='avatar', upload_to='img/users/avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        """
        :return: Returns the first_name plus the last_name, with a space in between.
        """
        full_name = f'{self.first_name} {self.last_name}'
        return full_name

    def get_short_name(self):
        """
        :return: Returns the short name for the user.
        """
        return self.first_name

    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     """
    #     Sends an email to this user.
    #     """
    #     send_mail(subject, message, from_email, [self.email], **kwargs)


class ClusterTag(models.Model):
    title = models.CharField(max_length=200, verbose_name='tag')


class Cluster(models.Model):
    headline = models.CharField(max_length=200, verbose_name='headline')
    content = models.TextField(verbose_name='cluster overlay')
    tags = models.ManyToManyField(ClusterTag, verbose_name='cluster tags')


class ClusterVote(models.Model):
    user = models.ForeignKey(User, verbose_name='linked user', on_delete=models.CASCADE)
    cluster = models.ForeignKey(Cluster, verbose_name='linked cluster')
    value = models.IntegerField(verbose_name='vote impact')

    class Meta:
        unique_together = ('user', 'cluster',)


class ClusterComment(models.Model):
    user = models.ForeignKey(User, verbose_name='linked user', on_delete=models.CASCADE)
    cluster = models.ForeignKey(Cluster, verbose_name='linked cluster')
    content = models.TextField(verbose_name='comment')


class ClusterCommentVote(models.Model):
    user = models.ForeignKey(User, verbose_name='linked user', on_delete=models.CASCADE)
    cluster_comment = models.ForeignKey(ClusterComment, verbose_name='linked cluster comment')
    value = models.IntegerField(verbose_name='vote impact')

    class Meta:
        unique_together = ('user', 'cluster_comment',)


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE)

    link = models.URLField(verbose_name='hyperlink')
    headline = models.CharField(max_length=200, verbose_name='headline')
    description = models.TextField(verbose_name='comment')
    content = models.TextField(verbose_name='quote')
    preview_picture = models.ImageField(verbose_name='preview picture', upload_to='img/posts/preview/', blank=True)

    clusters = models.ManyToManyField(Cluster, verbose_name='used in clusters')

    submission_datetime = models.DateTimeField(verbose_name='submission datetime', default=datetime.now, blank=True)
    is_published = models.BooleanField(default=False, blank=True, verbose_name='publication marker')
    publication_datetime = models.DateTimeField(verbose_name='publication datetime', default=datetime.now, blank=True)

    def publish(self):
        """
        :return: Marks the post published and sets its publication datetime
        """
        if not self.is_published:
            self.is_published = True
            self.publication_datetime = datetime.now()
            # TODO: also reposts

    def conceal(self):
        """
        :return: Marks the post not published
        """
        if self.is_published:
            self.is_published = False
            # TODO: also reposts


class PostVote(models.Model):
    user = models.ForeignKey(User, verbose_name='linked user', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='linked post')
    value = models.IntegerField(verbose_name='vote impact')

    class Meta:
        unique_together = ('user', 'post',)


class PostComment(models.Model):
    post = models.ForeignKey(Post, verbose_name='linked post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='linked user', on_delete=models.CASCADE)
    message = models.TextField(verbose_name='comment')


class PostCommentVote(models.Model):
    user = models.ForeignKey(User, verbose_name='linked user', on_delete=models.CASCADE)
    post_comment = models.ForeignKey(Post, verbose_name='linked post comment')
    value = models.IntegerField(verbose_name='vote impact')

    class Meta:
        unique_together = ('user', 'post_comment',)


class Repost(models.Model):
    user = models.ForeignKey(User, verbose_name='reposted by', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='post')
    publication_datetime = models.DateTimeField(verbose_name='publication datetime', default=datetime.now, blank=True)
