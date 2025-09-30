from django.urls import path
from .views import RegUserAPIView,LoginAPI

urlpatterns = [
    path('reg-user/', RegUserAPIView.as_view(), name='reg-user-api'),
    path('login/',LoginAPI.as_view(),name='login-user-api')
]