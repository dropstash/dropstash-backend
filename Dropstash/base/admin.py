from django.contrib import admin

from .models import Cluster, ClusterVote, ClusterComment, ClusterCommentVote, ClusterTag
from .models import Post, PostVote, PostComment, PostCommentVote, Repost

admin.site.register(Cluster)
admin.site.register(ClusterVote)
admin.site.register(ClusterComment)
admin.site.register(ClusterCommentVote)
admin.site.register(ClusterTag)

admin.site.register(Post)
admin.site.register(PostVote)
admin.site.register(PostComment)
admin.site.register(PostCommentVote)
admin.site.register(Repost)
