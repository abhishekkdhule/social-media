from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt


@api_view(['POST'])
@csrf_exempt
def create_post(request):
    return Response({"message": "Post created successfully!"}, status=201)

@api_view(['GET'])
@csrf_exempt
def get_posts(request):
    return Response({"message": "Posts retrieved successfully!"}, status=200)

@api_view(['DELETE'])
@csrf_exempt
def delete_post(request, post_id):
    return Response({"message": f"Post {post_id} deleted successfully!"}, status=200)

@api_view(['PUT'])
@csrf_exempt
def like_unlike_post(request, post_id):
    return Response({"message": f"Post {post_id} liked successfully!"}, status=200)

@api_view(['POST'])
@csrf_exempt
def comment_on_post(request, post_id):
    return Response({"message": f"Commented on post {post_id} successfully!"}, status=200)

@api_view(['DELETE'])
@csrf_exempt
def delete_comment(request, post_id, comment_id):
    return Response({"message": f"Comment {comment_id} deleted from post {post_id} successfully!"}, status=200)