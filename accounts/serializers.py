from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  # Ensure password is not returned in response
        }

    def validate(self, data):
        # Check if username already exists
        if User.objects.filter(username=data.get('username')).exists():
            raise serializers.ValidationError({'username': ['A user with that username already exists.']})

        # Check if email already exists
        if User.objects.filter(email=data.get('email')).exists():
            raise serializers.ValidationError({'email': ['A user with that email already exists.']})

        # Optional: Validate password (e.g., minimum length)
        password = data.get('password')
        if len(password) < 8:
            raise serializers.ValidationError({'password': ['Password must be at least 8 characters long.']})

        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
 

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        # Check if both email and password are provided
        if not email or not password:
            raise serializers.ValidationError({
                'error': 'Must include both email and password'
            })

        # Check if email exists in the database
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({
                'email': ['No account found with this email address.']
            })

        # Optional: Validate password (e.g., minimum length) before authentication
        if len(password) < 8:
            raise serializers.ValidationError({
                'password': ['Password must be at least 8 characters long.']
            })

        # Authenticate the user
        user = authenticate(request=self.context.get('request'), email=email, password=password)
        if not user:
            raise serializers.ValidationError({
                'password': ['Incorrect password.']
            })

        # Store the authenticated user in validated data
        data['user'] = user
        return data