from rest_framework.routers import SimpleRouter
from . import views
from django.urls import path

app_name = 'accounts'
router = SimpleRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    path('custom/', views.CustomView.as_view(), name='custom'),
    path('my/', views.MyEndpoint.as_view(), name='custom'),
] + router.urls
