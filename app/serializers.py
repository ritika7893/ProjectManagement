from rest_framework import serializers
from .models import  UserReg

class RegUserSerializer(serializers.ModelSerializer):
    class Meta:
        model =UserReg
        fields = ['user_id', 'name', 'email', 'password','role']
class LoginSerializer(serializers.Serializer):
    email_or_phone = serializers.CharField()
    password = serializers.CharField()