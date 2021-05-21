from django.shortcuts import render
from rest_framework import generics, serializers
from .serializers import UserSerializer, TaskSerializer
from django.contrib.auth.hashers import make_password
from django_filters import rest_framework as filters
from .models import Task, User


# Create your views here.

class UserCreateAPIView(generics.CreateAPIView):

    serializer_class = UserSerializer

    # 個々の処理をUserSerializerのsaveの部分で任せてもよいかも
    def perform_create(self, serializer):
        raw_password = serializer.validated_data['password']
        hashed_password = make_password(raw_password)
        serializer.save(password=hashed_password)

class UserPasswordUpdateAPIView(generics.UpdateAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user

    def perform_update(self, serializer):
        raw_password = serializer.validated_data['password']
        hashed_password = make_password(raw_password)
        serializer.save(password=hashed_password)
    '''
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        print("okey")
        print(response)
        return response
    '''

class UserProfileUpdateAPIView(generics.UpdateAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user
    '''
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        print("okey")
        print(response)
        return response
    '''

        
class UserEditAPIView(generics.RetrieveAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()

class TaskCreateAPIView(generics.CreateAPIView):

    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        request.data['user_id'] = request.user.id
        response = super().create(request, *args, **kwargs)
        return response
'''
class TaskFilter(filters.FilterSet):

    class Meta:
        model = Task
        fields = ['user__id']

    @property
    def qs(self):
        parent = super().qs
        user = getattr(self.request, 'user', None)
        print(user)
        return parent.filter()
'''
class TaskListAPIView(generics.ListAPIView):

    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    # filter_backends = [ filters.DjangoFilterBackend ]
    # filterset_class = TaskFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__id=self.request.user.id)
    '''
    def list(self, request, *args, **kwargs):
        request.query_params['user__id'] = request.user.id
        
        response = super().list(request, *args, **kwargs)
        return response
    '''
class TaskEditAPIView(generics.RetrieveAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskUpdateAPIView(generics.UpdateAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer