from ast import Not
import profile
from time import sleep
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import ProfileSerializer, PostSerializer, CommentSerializer, StorySerializer
from instagram.models import Notification, Profile, Post, Comment, Story
from rest_framework.permissions import IsAuthenticated
from api import serializers


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/',
        '/api/posts/',
    ]
    return Response(routes)


@api_view(['GET'])
def getPosts(request):
    projects = Post.objects.all()
    serializer = PostSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like(request, pk):
    post = Post.objects.get(id=pk)
    user = request.user.profile
    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)

        if not Notification.objects.filter(
            user_to_notify=post.owner,
            user=user,
            post=post,
        ).exists():

            Notification.objects.create(
                user_to_notify=post.owner,
                user=user,
                post=post,
            )

    return Response('Liked')


@api_view(['GET'])
def getComments(request, pk):
    comments = Comment.objects.filter(post=pk)
    serializer = CommentSerializer(comments, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):

    profile = request.user.profile
    serializer = ProfileSerializer(profile, many=False)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
def getStories(request):

    stories = Story.objects.all()
    serializer = StorySerializer(stories, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getStorie(request, pk):

    storie = Story.objects.filter(id=pk)
    serializer = StorySerializer(storie, many=True)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createPost(request):
    data = request.data
    post = Post.objects.create(
        owner=request.user.profile,
        caption=data['caption'],
        image=data['image'],
    )
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserPosts(request):

    posts = Post.objects.filter(owner=request.user.profile)
    serializer = PostSerializer(posts, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotifications(request):
    notifications = Notification.objects.filter(
        user_to_notify=request.user.profile)
    serializer = serializers.NotificationSerializer(notifications, many=True)

    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createComment(request):
    data = request.data
    comment = Comment.objects.create(
        post=Post.objects.get(id=data['post']),
        user=request.user.profile,
        body=data['comment'],
    )
    serializer = CommentSerializer(comment, many=False)
    return Response(serializer.data)