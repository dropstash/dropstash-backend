from django.contrib import admin

from .models import User
from .models import Cluster, ClusterVote, ClusterComment, ClusterCommentVote, ClusterTag
from .models import Post, PostVote, PostComment, PostCommentVote, Repost


class ClusterCommentInline(admin.StackedInline):
    model = ClusterComment
    extra = 1


class ClusterCommentVoteInline(admin.StackedInline):
    model = ClusterCommentVote
    extra = 1


class ClusterVoteInline(admin.StackedInline):
    model = ClusterVote
    extra = 1


class PostCommentInline(admin.StackedInline):
    model = PostComment
    extra = 1


class PostCommentVoteInline(admin.StackedInline):
    model = PostCommentVote
    extra = 1


class PostVoteInline(admin.StackedInline):
    model = PostVote
    extra = 1
