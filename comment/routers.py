from rest_framework import routers
from comment import views


router = routers.DefaultRouter()
router.register(r'comments', views.CommentViewSet,base_name='comment')