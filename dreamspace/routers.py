from rest_framework import routers
from dreamspace import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)