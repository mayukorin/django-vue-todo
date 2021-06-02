from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import check_password
from .models import User, Task

class UserSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'confirm_password']
        extra_fields = {
            'email': {
                'validators':[
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message='そのメールアドレスは，既にほかのユーザが使っています',
                    )
                ]
            },
            'password': {
                'write_only': True
            }
        }

    def validate(self, data):
        confirm_password = data.get('confirm_password')
        if confirm_password is None:
            return data
        previous_password = self.instance.password
        if check_password(confirm_password, previous_password) is False:
            raise serializers.ValidationError("現在のパスワードが間違っています")
        return data


class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    class Meta:
        model = Task
        fields = ['pk', 'title', 'content', 'deadline', 'user', 'user_id']

    def create(self, validated_data):
        validated_data['user'] = validated_data.get('user_id', None)

        if validated_data['user'] is None:
            raise serializers.ValidationError("User not found.")

        del validated_data['user_id']

        return Task.objects.create(**validated_data)