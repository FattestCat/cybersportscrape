from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from PostData import views

router = routers.DefaultRouter()
router.register(r'postdata', views.PostViewSet)
router.register(r'word', views.WordViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api/', include('rest_framework.urls'), name = 'rest_framework'),
]
