from rest_framework import serializers
from instagram.models import Post, Comment, Profile, Story, User, Notification


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()


    class Meta:
        model = Profile
        fields = '__all__'
        
    def __str__(self):
        return str(self.user.username)


class PostSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = ProfileSerializer(many=False)

    class Meta:
        model = Comment
        fields = '__all__'


class StorySerializer(serializers.ModelSerializer):
    user = ProfileSerializer(many=False)

    class Meta:
        model = Story
        fields = '__all__'
class NotificationSerializer(serializers.ModelSerializer):
    user = ProfileSerializer(many=False)
    user_to_notify = ProfileSerializer(many=False)
    post = PostSerializer(many=False)

    class Meta:
        model = Notification
        fields = '__all__'