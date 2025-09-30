from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
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
class LoginAPI(APIView):
    
    def post(self, request):
        email_or_phone = request.data.get('email_or_phone')
        password = request.data.get('password')

        if not email_or_phone or not password:
            return Response({"error": "Email/Phone and Password are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Match either email or phone
            user =UserReg.objects.get(email=email_or_phone) if '@' in email_or_phone else UserReg.objects.get(phone=email_or_phone)

            # Verify password
            if check_password(password, user.password):
                return Response({
                    "unique_id": user.user_id,
                    "role": user.role
                }, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid Password"}, status=status.HTTP_401_UNAUTHORIZED)

        except UserReg.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)