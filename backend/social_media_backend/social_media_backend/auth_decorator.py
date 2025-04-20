from django.http import JsonResponse
from firebase_admin import auth
from rest_framework import status

def is_authenticated_user(func):
    """
    Decorator to check if the user is authenticated.
    """
    def wrapper(*args, **kwargs):
        try:
            request = args[0]
            token = request.headers.get("Authorization")
            bearer_token = token.split(" ")[-1]
            if not bearer_token or not auth.verify_id_token(bearer_token):
                return JsonResponse(data={"message": "User not authorized."}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return JsonResponse(data={"message": "User not authorized."}, status=status.HTTP_401_UNAUTHORIZED)
        return func(*args, **kwargs)
    return wrapper