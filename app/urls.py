from django.urls import path
from .views import RegUserAPIView

urlpatterns = [
    path('reg-users/', RegUserAPIView.as_view(), name='reg-user-api'),
    
]