from rest_framework import serializers
from comment.models import Comment

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='blog:comment-detail',
    )
    class Meta:
        model = Comment
        fields = ('url','id', 'text','created_time','user')