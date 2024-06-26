
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from post.serializers import PostListSerializer, CommentListSerializer
from .models import *


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id','first_name','last_name','username','email','password']

class UserBadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBadge
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = '__all__'

class ProfileListSerializer(serializers.ModelSerializer):
    net_vote = serializers.SerializerMethodField()
    net_points = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'user', 'profile_pic', 'bio', 'verified_org', 'net_vote','net_points']

    def get_net_vote(self, obj):
        upvotes = sum([post.upvote.count() for post in obj.posts.all()]) + sum([post.upvote.count() for post in obj.my_comments.all()])
        downvotes = sum([post.downvote.count() for post in obj.posts.all()]) + sum([post.downvote.count() for post in obj.my_comments.all()])
        net_vote = upvotes - downvotes
        return net_vote
    
    def get_net_points(self, obj):
        total_points = Point.objects.filter(user_profile=obj).aggregate(total_points=models.Sum('value'))
        net_points = total_points['total_points'] if total_points['total_points'] else 0
        return net_points

class ProfileDetailSerializer(serializers.ModelSerializer):
    net_vote = serializers.SerializerMethodField()
    net_points = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [ 'user','id', 'profile_pic', 'org_email', 'bio', 'verified_org', 'net_vote', 'net_points']

    def get_net_vote(self, obj):
        upvotes = sum([post.upvote.count() for post in obj.posts.all()]) + sum([post.upvote.count() for post in obj.my_comments.all()])
        downvotes = sum([post.downvote.count() for post in obj.posts.all()]) + sum([post.downvote.count() for post in obj.my_comments.all()])
        net_vote = upvotes - downvotes
        return net_vote
    
    def get_net_points(self, obj):
        total_points = Point.objects.filter(user_profile=obj).aggregate(total_points=models.Sum('value'))
        net_points = total_points['total_points'] if total_points['total_points'] else 0
        return net_points
