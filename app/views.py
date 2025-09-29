from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .utils import generate_user_id
from .models import UserReg
from .serializers import RegUserSerializer
from django.contrib.auth.hashers import make_password

class RegUserAPIView(APIView):

    def get(self, request):
        users = UserReg.objects.all()
        serializer = RegUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()

        if 'user_id' not in data or not data['user_id']:
            data['user_id'] = generate_user_id(prefix="USR")

        if 'user_status' not in data or not data['user_status']:
            data['user_status'] = 'active'

        raw_password = data.get('password')  # keep original password for reuse
        if raw_password:
            data['password'] = make_password(raw_password)

        serializer = RegUserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User Registered Successfully"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)