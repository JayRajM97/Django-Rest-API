from rest_framework import serializers
from . import models

#name = serializers.CharField(max_length=10)
class HelloSerializer(serializers.Serializer):
    """Serialize a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our User Profile Object."""

    #meta class defines what we want to take from our model
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and Returns new user"""

        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
