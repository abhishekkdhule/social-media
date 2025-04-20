
# User Views
#Signup, Signin, Signinout, Profile, Update Profile, Change Password, Delete Account
from rest_framework.response import Response
from rest_framework import status

from social_media_backend.auth_decorator import is_authenticated_user

# from ..social_media_backend.auth_decorator import is_authenticated_user
from .serializers import UserSigninSerializer, UserSignupSerializer 
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
import firebase_admin
from firebase_admin import credentials, firestore
from rest_framework.parsers import JSONParser


@api_view(['POST'])
@csrf_exempt
def signup(request):
    data = JSONParser().parse(request)
    user_signup_serializer = UserSignupSerializer(data=data)
    if user_signup_serializer.is_valid():
        user_signup_serializer.save()
        return Response(data=user_signup_serializer.data, status=status.HTTP_201_CREATED)
    return Response(data=user_signup_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@csrf_exempt
def signin(request):
    data = JSONParser().parse(request)
    user_signin_serializer = UserSigninSerializer(data=data)
    if user_signin_serializer.is_valid():
        return Response(data=user_signin_serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

def signout(request):   
    return Response(status=status.HTTP_200_OK)  

@is_authenticated_user
@api_view(['GET'])
@csrf_exempt
def test(request):
    print("authenticated")
    return Response({"message": "Hello World!"}, status=status.HTTP_200_OK)

