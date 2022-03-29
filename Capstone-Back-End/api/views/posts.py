from turtle import update
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.post import PostSerializer, PostPostSerializer 
from ..models.post import Post
from rest_framework import status
from django.shortcuts import get_object_or_404



class PostsView(APIView):
    def get(self, request):
        posts = Post.objects.filter(author=request.user.id)
        data = PostSerializer(posts, many=True).data
        return Response(data)

    def post(self, request):
        request.data['author'] = request.user.id
        post = PostPostSerializer(data=request.data)
        if post.is_valid():
            post.save()
            return Response(post.data, status=status.HTTP_201_CREATED)
        else:
            return Response(post.errors, status=status.HTTP_400_BAD_REQUEST)

class PostView(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        data = PostSerializer(post).data
        return Response(data)
    
    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        updated_post = PostSerializer(post, data=request.data)
        if updated_post.is_valid():
            updated_post.save()
            return Response(updated_post.data)
        else:
            return Response(updated_post.errors, status=status.HTTP_400_BAD_REQUEST)