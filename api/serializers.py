from authapp.models import MyUser
from customer.models import Event
from rest_framework import serializers


class ReadEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['name', 'role', 'email', 'password', 'phone', 'date_of_birth']

    def create(self, validated_data):
        return MyUser.objects.create_user(name=validated_data['name'],
                                          email=validated_data['email'],
                                          password=validated_data['password'],
                                          phone=validated_data['phone'],
                                          date_of_birth=validated_data['date_of_birth'],
                                          role='CUSTOMER')


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)
