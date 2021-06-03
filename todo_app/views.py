from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, TaskSerializer
from .models import Task, User


# Create your views here.


class UserCreateAPIView(generics.CreateAPIView):

    serializer_class = UserSerializer


class UserPasswordUpdateAPIView(generics.UpdateAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class UserProfileUpdateAPIView(generics.UpdateAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class UserEditAPIView(generics.RetrieveAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)


class TaskCreateAPIView(generics.CreateAPIView):

    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        request.data["user_id"] = request.user.id
        response = super().create(request, *args, **kwargs)
        return response


class TaskListAPIView(generics.ListAPIView):

    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__id=self.request.user.id)


class TaskEditAPIView(generics.RetrieveAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)


class TaskUpdateAPIView(generics.UpdateAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)


class TaskDeleteAPIView(generics.DestroyAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
