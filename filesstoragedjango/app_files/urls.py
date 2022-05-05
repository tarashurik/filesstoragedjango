from rest_framework import routers
from app_files import views


router = routers.DefaultRouter()
router.register(r'files', views.FileUploadViewSet, basename='files_queryset')

urlpatterns = router.urls
