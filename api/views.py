from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status, authentication, permissions, generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from api.serializers import ReadEventSerializer, UserCreationSerializer, LoginSerializer
from customer.models import Event
from rest_framework_simplejwt.authentication import JWTAuthentication



class EventsMixin(generics.GenericAPIView,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin
                 ):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [
                              JWTAuthentication
                              ]
    queryset = Event.objects.all()
    serializer_class = ReadEventSerializer

    # def get_queryset(self):
    #     user = self.request.user
    #     return Event.objects.filter(host=user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)




class Registration(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserCreationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def perform_create(self, serializer):
    #     serializer.save(role='CUSTOMER')


class Login(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                print(token)
                print(created)


                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    def get(self, request):
        logout(request)
        return Response({'msg': 'session ended'})