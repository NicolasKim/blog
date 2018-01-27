from rest_framework import serializers
from blog.models import Post, Category, Tag
from django.contrib.auth.models import User

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='blog:category-detail',
    )
    class Meta:
        model = Category
        fields = ('url','id', 'name')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='blog:tag-detail',
    )
    class Meta:
        model = Tag
        fields = ('url','id', 'name')


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='blog:blog-detail',
    )
    category = serializers.HyperlinkedRelatedField(
        view_name='blog:category-detail',
        many=False,
        read_only=False,
        queryset=Category.objects.all()
    )
    tags = serializers.HyperlinkedRelatedField(
        view_name='blog:tag-detail',
        many=True,
        read_only=False,
        queryset=Tag.objects.all()
    )

    author = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        many=False,
        read_only=False,
        queryset=User.objects.all()
    )


    class Meta:
        model = Post
        fields = ('url',
                  'id',
                  'title',
                  'cover_image',
                  'excerpt',
                  'author',
                  'views',
                  'body',
                  'category',
                  'tags',
                  'created_time',
                  'modified_time',
                  )
