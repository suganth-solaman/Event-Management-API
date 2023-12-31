from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    conform_password = serializers.CharField(write_only=True)
    is_staff = serializers.BooleanField(required=False)
    admin = serializers.BooleanField(required=False)

    def validate(self, attrs):
        if attrs['password'] != attrs['conform_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return attrs

    def create(self, validated_data):
        is_staff = validated_data.pop('admin', False)
        validated_data.pop('conform_password')
        user = User.objects.create_user(**validated_data)
        user.is_staff = is_staff
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'password', 'conform_password', 'admin', 'is_staff', 'email')


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')