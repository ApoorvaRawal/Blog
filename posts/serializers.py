from rest_framework import serializers
from posts.models import Category,Post,Comment,User
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    



class Categoryserializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'


        
        
                                 

class Postserializers(serializers.ModelSerializer):
    category=Categoryserializers(many=True,source='Categories',read_only=True)
    author=UserSerializer(many=False,read_only=True)
    
    class Meta:
        model=Post
        fields = '__all__'
        

class Commentserializers(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    posts=serializers.ReadOnlyField(source='post.title')

    class Meta:
        model=Comment
        fields='__all__'
        



