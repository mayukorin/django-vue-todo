from django.test import TestCase
from ..models import Task
from ..serializers import TaskSerializer, UserSerializer
from django.contrib.auth import get_user_model


class TestUserSerializer(TestCase):
    def test_input_valid(self):

        input_data = {"email": "aa@example.com", "username": "abc", "password": "abc"}
        serializer = UserSerializer(data=input_data)
        self.assertEqual(serializer.is_valid(), True)

    def test_input_if_email_is_blank(self):

        input_data = {"email": "", "username": "abc", "password": "abc"}
        serializer = UserSerializer(data=input_data)
        self.assertEqual(serializer.is_valid(), False)
        self.assertCountEqual(serializer.errors.keys(), ["email"])
        self.assertCountEqual(
            [str(x) for x in serializer.errors["email"]],
            ["この項目は空にできません。"],
        )

    def test_input_if_username_is_blank(self):

        input_data = {"email": "aa@example.com", "username": "", "password": "abc"}
        serializer = UserSerializer(data=input_data)
        self.assertEqual(serializer.is_valid(), False)
        self.assertCountEqual(serializer.errors.keys(), ["username"])
        self.assertCountEqual(
            [str(x) for x in serializer.errors["username"]],
            ["この項目は空にできません。"],
        )

    def test_input_if_password_is_blank(self):

        input_data = {"email": "aa@example.com", "username": "abc", "password": ""}
        serializer = UserSerializer(data=input_data)
        self.assertEqual(serializer.is_valid(), False)
        self.assertCountEqual(serializer.errors.keys(), ["password"])
        self.assertCountEqual(
            [str(x) for x in serializer.errors["password"]],
            ["この項目は空にできません。"],
        )

    def test_input_if_email_is_same(self):

        input_data = {"email": "aa@example.com", "username": "abc", "password": "abc"}
        serializer = UserSerializer(data=input_data)
        serializer.is_valid()
        serializer.save()

        input_data = {"email": "aa@example.com", "username": "aaa", "password": "aaa"}
        serializer = UserSerializer(data=input_data)
        self.assertEqual(serializer.is_valid(), False)
        self.assertCountEqual(serializer.errors.keys(), ["email"])
        self.assertCountEqual(
            [str(x) for x in serializer.errors["email"]],
            ["そのメールアドレスは，既にほかのユーザが使っています"],
        )

    def test_input_if_email_is_too_long(self):

        long_email = ""
        for _ in range(255):
            long_email += "a"

        long_email += "@example.com"
        # print(long_email)
        input_data = {"email": long_email, "username": "aaa", "password": "aaa"}
        serializer = UserSerializer(data=input_data)
        self.assertEqual(serializer.is_valid(), False)
        self.assertCountEqual(serializer.errors.keys(), ["email"])
        self.assertCountEqual(
            [str(x) for x in serializer.errors["email"]],
            ["この項目が255文字より長くならないようにしてください。"],
        )

    def test_input_if_username_is_too_long(self):

        long_username = ""
        for _ in range(151):
            long_username += "a"

        input_data = {
            "email": "aaa@example.com",
            "username": long_username,
            "password": "aaa",
        }
        serializer = UserSerializer(data=input_data)
        self.assertEqual(serializer.is_valid(), False)
        self.assertCountEqual(serializer.errors.keys(), ["username"])
        self.assertCountEqual(
            [str(x) for x in serializer.errors["username"]],
            ["この項目が150文字より長くならないようにしてください。"],
        )

    def test_output_data(self):
        user = get_user_model().objects.create_user(
            email="pp@example.com", username="abc", password="abc"
        )
        serializer = UserSerializer(instance=user)
        expected_data = {"email": user.email, "username": user.username}
        self.assertDictEqual(serializer.data, expected_data)

    def test_update_user_model(self):
        user = get_user_model().objects.create_user(
            email="pp@example.com", username="abc", password="abc"
        )
        input_data = {"email": "aaa@example.com", "confirm_password": "abc"}
        serializer = UserSerializer(instance=user, data=input_data, partial=True)
        self.assertEqual(serializer.is_valid(), True)

    def test_update_user_model_if_wrong_confirm_password(self):
        user = get_user_model().objects.create_user(
            email="pp@example.com", username="abc", password="abc"
        )
        input_data = {"email": "aaa@example.com", "confirm_password": "aaa"}
        serializer = UserSerializer(instance=user, data=input_data, partial=True)
        self.assertEqual(serializer.is_valid(), False)
        self.assertCountEqual(serializer.errors.keys(), ["non_field_errors"])
        self.assertCountEqual(
            [str(x) for x in serializer.errors["non_field_errors"]],
            ["現在のパスワードが間違っています"],
        )


class TestTaskSerializer(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = get_user_model().objects.create_user(
            email="xx@example.com", username="abc", password="abc"
        )

    def test_input_valid(self):

        input_data = {
            "title": "abc",
            "content": "abc",
            "deadline": "2021-06-08",
            "user_id": self.user.pk,
        }
        serializer = TaskSerializer(data=input_data)
        self.assertEqual(serializer.is_valid(), True)

    def test_input_valid_if_content_is_blank(self):

        input_data = {
            "title": "abc",
            "content": "",
            "deadline": "2021-06-08",
            "user_id": self.user.pk,
        }
        serializer = TaskSerializer(data=input_data)
        self.assertEqual(serializer.is_valid(), True)

    def test_input_valid_if_deadline_is_blank(self):

        input_data = {
            "title": "abc",
            "content": "abc",
            "deadline": None,
            "user_id": self.user.pk,
        }
        serializer = TaskSerializer(data=input_data)
        self.assertEqual(serializer.is_valid(), True)

    def test_input_valid_if_title_is_blank(self):

        input_data = {
            "title": "",
            "content": "abc",
            "deadline": "2021-06-08",
            "user_id": self.user.pk,
        }
        serializer = TaskSerializer(data=input_data)
        self.assertEqual(serializer.is_valid(), False)
        self.assertCountEqual(serializer.errors.keys(), ["title"])
        self.assertCountEqual(
            [str(x) for x in serializer.errors["title"]],
            ["この項目は空にできません。"],
        )

    def test_input_valid_if_user_id_is_blank(self):

        input_data = {
            "title": "abc",
            "content": "abc",
            "deadline": "2021-06-08",
            "user_id": None,
        }
        serializer = TaskSerializer(data=input_data)
        self.assertEqual(serializer.is_valid(), False)
        self.assertCountEqual(serializer.errors.keys(), ["user_id"])
        self.assertCountEqual(
            [str(x) for x in serializer.errors["user_id"]],
            ["この項目はnullにできません。"],
        )

    def test_output_data(self):

        task = Task.objects.create(
            title="abc", content="abc", deadline=None, user=self.user
        )
        serializer = TaskSerializer(instance=task)
        self.assertEqual(serializer.data["title"], task.title)
        self.assertEqual(serializer.data["content"], task.content)
        self.assertEqual(serializer.data["deadline"], task.deadline)
        self.assertEqual(serializer.data["user"]["email"], self.user.email)
