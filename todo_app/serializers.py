from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import check_password, make_password
from .models import User, Task


class UserSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(required=False, write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "username", "confirm_password"]
        extra_kwargs = {
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="そのメールアドレスは，既にほかのユーザが使っています",
                    )
                ]
            },
            "password": {"write_only": True},
        }

    def validate(self, data):
        confirm_password = data.get("confirm_password")

        if self.instance is None or confirm_password is None:
            return data
        if self.instance.check_password(confirm_password) is False:
            raise serializers.ValidationError("現在のパスワードが間違っています")
        return data

    def update(self, instance, validated_data):
        raw_password = validated_data.get("password")
        if raw_password is not None:
            instance.set_password(raw_password)
        return super().update(instance, validated_data)

    def create(self, validated_data):
       
        return User.objects.create_user(request_data=validated_data)


class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True
    )

    class Meta:
        model = Task
        fields = ["pk", "title", "content", "deadline", "user", "user_id"]

    def create(self, validated_data):
        validated_data["user"] = validated_data.get("user_id", None)

        if validated_data["user"] is None:
            raise serializers.ValidationError("User not found.")

        del validated_data["user_id"]

        return super().create(validated_data)
