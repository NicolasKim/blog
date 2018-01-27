from rest_framework import viewsets,pagination
from comment.models import Comment
from comment.serializer import CommentSerializer

class CommentResultsSetPagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.order_by('-created_time')
    serializer_class = CommentSerializer
    pagination_class = CommentResultsSetPagination
