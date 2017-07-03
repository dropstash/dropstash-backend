from django.contrib import admin

from .models import User
from .models import Cluster, ClusterComment, ClusterTag
from .models import Post, PostComment, Repost
from .inlines import ClusterCommentInline, ClusterCommentVoteInline, ClusterVoteInline
from .inlines import PostCommentInline, PostCommentVoteInline, PostVoteInline


class ClusterCommentAdmin(admin.ModelAdmin):
    inlines = [
        ClusterCommentVoteInline,
    ]


class ClusterAdmin(admin.ModelAdmin):
    inlines = [
        ClusterCommentInline,
        ClusterVoteInline,
    ]


class PostCommentAdmin(admin.ModelAdmin):
    inlines = [
        PostCommentVoteInline,
    ]


class PostAdmin(admin.ModelAdmin):
    inlines = [
        PostCommentInline,
        PostVoteInline,
    ]

admin.site.register(User)

admin.site.register(Cluster, ClusterAdmin)
admin.site.register(ClusterComment, ClusterCommentAdmin)
admin.site.register(ClusterTag)

admin.site.register(Post, PostAdmin)
admin.site.register(PostComment, PostCommentAdmin)
admin.site.register(Repost)
