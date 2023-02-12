from rest_framework.routers import DefaultRouter
from .views import BookViewSet


router = DefaultRouter()

router.register('user', BookViewSet, basename='users')



urlpatterns = router.urls