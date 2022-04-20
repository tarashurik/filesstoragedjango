from rest_framework import routers
from app_users import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = router.urls
