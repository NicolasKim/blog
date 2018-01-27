from rest_framework import routers
from blog import views


router = routers.DefaultRouter()
router.register(r'blogs', views.BlogViewSet,base_name='blog')
router.register(r'categorys',views.CategoryViewSet)
router.register(r'tags',views.TagViewSet)