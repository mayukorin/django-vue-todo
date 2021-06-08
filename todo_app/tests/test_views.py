from django.contrib.auth.hashers import check_password
from rest_framework.test import APITestCase
from ..models import Task, User
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken


class TestUserCreateAPIView(APITestCase):

    TARGET_URL = "/todo/user/create/"

    def test_create_success(self):

        params = {
            "email": "pp@example.com",
            "username": "abc",
            "password": "abc",
        }
        response = self.client.post(self.TARGET_URL, params, format="json")
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, 201)
        user = User.objects.get()
        expected_json_dict = {"email": user.email, "username": user.username}
        self.assertJSONEqual(response.content, expected_json_dict)

    def test_create_bad_request_with_same_email(self):

        params = {
            "email": "pp@example.com",
            "username": "abc",
            "password": "abc",
        }
        response = self.client.post(self.TARGET_URL, params, format="json")
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, 201)
        user = User.objects.get()
        expected_json_dict = {"email": user.email, "username": user.username}
        self.assertJSONEqual(response.content, expected_json_dict)

        params = {
            "email": "pp@example.com",
            "username": "xxx",
            "password": "xxx",
        }
        response = self.client.post(self.TARGET_URL, params, format="json")
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, 400)


class TESTUserPasswordUpdateAPIView(APITestCase):

    TARGET_URL = "/todo/password/update/"

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # pk=1
        cls.user = get_user_model().objects.create_user(
            email="pp@example.com", username="abc", password="abc"
        )

    def test_update_success(self):

        token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION="JWT " + token)
        params = {"password": "cba", "confirm_password": "abc"}
        response = self.client.patch(self.TARGET_URL, params, format="json")
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, 200)
        user = User.objects.get()
        expected_json_dict = {"email": user.email, "username": user.username}
        self.assertJSONEqual(response.content, expected_json_dict)
        self.assertTrue(check_password("cba", user.password))

    def test_update_bad_request_with_wrong_confirm_password(self):

        token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION="JWT " + token)
        params = {"password": "cba", "confirm_password": "aaa"}
        response = self.client.patch(self.TARGET_URL, params, format="json")
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, 400)


class TESTUserProfileUpdateAPIView(APITestCase):

    TARGET_URL = "/todo/user/profile/update/"

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # pk=2
        cls.user = get_user_model().objects.create_user(
            email="pp@example.com", username="abc", password="abc"
        )
        # pk=3
        get_user_model().objects.create_user(
            email="xx@example.com", username="abc", password="abc"
        )

    def test_update_username_success(self):

        token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION="JWT " + token)

        params = {"username": "xxx", "confirm_password": "abc"}
        response = self.client.patch(self.TARGET_URL, params, format="json")
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.status_code, 200)
        updated_user = User.objects.get(pk=self.user.id)
        expected_json_dict = {
            "email": updated_user.email,
            "username": updated_user.username,
        }
        self.assertJSONEqual(response.content, expected_json_dict)

    def test_update_email_success(self):

        token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION="JWT " + token)

        params = {"email": "xxx@example.com", "confirm_password": "abc"}
        response = self.client.patch(self.TARGET_URL, params, format="json")
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.status_code, 200)
        updated_user = User.objects.get(pk=self.user.id)
        expected_json_dict = {
            "email": updated_user.email,
            "username": updated_user.username,
        }
        self.assertJSONEqual(response.content, expected_json_dict)

    def test_update_bad_request_with_wrong_confirm_password(self):

        token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION="JWT " + token)

        params = {"username": "xxx", "confirm_password": "aaa"}
        response = self.client.patch(self.TARGET_URL, params, format="json")
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.status_code, 400)

    def test_update_bad_request_with_same_email(self):

        token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION="JWT " + token)

        params = {"email": "xx@example.com", "confirm_password": "abc"}
        response = self.client.patch(self.TARGET_URL, params, format="json")
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.status_code, 400)


class TESTTaskCreateAPIView(APITestCase):

    TARGET_URL = "/todo/task/create/"

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # pk=4
        cls.user = get_user_model().objects.create_user(
            email="xx@example.com", username="abc", password="abc"
        )

    def test_create_success_full_input(self):

        token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION="JWT " + token)

        params = {"title": "abc", "content": "abc", "deadline": "2021-06-07"}
        response = self.client.post(self.TARGET_URL, params, format="json")
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(response.status_code, 201)
        task = Task.objects.get()
        expected_json_dict = {
            "pk": task.pk,
            "title": task.title,
            "content": task.content,
            "deadline": task.deadline.strftime("%Y-%m-%d"),
            "user": {"email": self.user.email, "username": self.user.username},
        }
        self.assertJSONEqual(response.content, expected_json_dict)

    def test_create_success_with_blank_content(self):

        token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION="JWT " + token)

        params = {"title": "abc", "content": "", "deadline": "2021-06-07"}
        response = self.client.post(self.TARGET_URL, params, format="json")
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(response.status_code, 201)
        task = Task.objects.get()
        expected_json_dict = {
            "pk": task.pk,
            "title": task.title,
            "content": task.content,
            "deadline": task.deadline.strftime("%Y-%m-%d"),
            "user": {"email": self.user.email, "username": self.user.username},
        }
        self.assertJSONEqual(response.content, expected_json_dict)

    def test_create_success_with_blank_deadline(self):

        token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION="JWT " + token)

        params = {"title": "abc", "content": "", "deadline": None}
        response = self.client.post(self.TARGET_URL, params, format="json")
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(response.status_code, 201)
        task = Task.objects.get()
        expected_json_dict = {
            "pk": task.pk,
            "title": task.title,
            "content": task.content,
            "deadline": None,
            "user": {"email": self.user.email, "username": self.user.username},
        }
        self.assertJSONEqual(response.content, expected_json_dict)

    def test_create_bad_request_with_blank_title(self):

        token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION="JWT " + token)

        params = {"title": "", "content": "abc", "deadline": "2021-06-07"}
        response = self.client.post(self.TARGET_URL, params, format="json")
        self.assertEqual(Task.objects.count(), 0)
        self.assertEqual(response.status_code, 400)


class TESTTaskUPDATEAPIView(APITestCase):

    TARGET_URL = "/todo/task/update/"
    TASKCREATE_URL = "/todo/task/create/"

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = get_user_model().objects.create_user(
            email="xx@example.com", username="abc", password="abc"
        )

    def test_update_success(self):

        token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION="JWT " + token)
        params = {"title": "abc", "content": "abc", "deadline": "2021-06-07"}
        response = self.client.post(self.TASKCREATE_URL, params, format="json")
        self.assertEqual(Task.objects.count(), 1)

        task = Task.objects.get()
        params = {"title": "aaa", "content": "aaa", "deadline": "2021-06-08"}
        response = self.client.patch(
            self.TARGET_URL + str(task.pk) + "/", params, format="json"
        )
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(response.status_code, 200)
        task = Task.objects.get()
        expected_json_dict = {
            "pk": task.pk,
            "title": task.title,
            "content": task.content,
            "deadline": task.deadline.strftime("%Y-%m-%d"),
            "user": {"email": self.user.email, "username": self.user.username},
        }
        self.assertJSONEqual(response.content, expected_json_dict)

    def test_update_bad_request_with_blank_title(self):

        token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION="JWT " + token)

        params = {"title": "abc", "content": "abc", "deadline": "2021-06-07"}
        response = self.client.post(self.TASKCREATE_URL, params, format="json")
        self.assertEqual(Task.objects.count(), 1)

        task = Task.objects.get()
        params = {"title": "", "content": "aaa", "deadline": "2021-06-08"}
        response = self.client.patch(
            self.TARGET_URL + str(task.pk) + "/", params, format="json"
        )
        self.assertEqual(response.status_code, 400)


class TESTTaskDeleteAPIView(APITestCase):

    TARGET_URL = "/todo/task/delete/"
    TASKCREATE_URL = "/todo/task/create/"

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = get_user_model().objects.create_user(
            email="xx@example.com", username="abc", password="abc"
        )

    def test_delete_success(self):

        token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION="JWT " + token)

        params = {"title": "abc", "content": "abc", "deadline": "2021-06-07"}
        response = self.client.post(self.TASKCREATE_URL, params, format="json")
        self.assertEqual(Task.objects.count(), 1)

        task = Task.objects.get()
        response = self.client.delete(
            self.TARGET_URL + str(task.pk) + "/", params, format="json"
        )
        self.assertEqual(response.status_code, 204)

    def test_delete_bad_requeset_with_non_exist_task_pk(self):

        token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION="JWT " + token)

        params = {"title": "abc", "content": "abc", "deadline": "2021-06-07"}
        response = self.client.post(self.TASKCREATE_URL, params, format="json")
        self.assertEqual(Task.objects.count(), 1)
        response = self.client.delete(
            self.TARGET_URL + str(0) + "/", params, format="json"
        )
        self.assertEqual(response.status_code, 404)


class TESTTaskListAPIView(APITestCase):

    TARGET_URL = "/todo/task/list/"
    TASKCREATE_URL = "/todo/task/create/"

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = get_user_model().objects.create_user(
            email="xx@example.com", username="abc", password="abc"
        )

    def test_list_success(self):

        token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION="JWT " + token)

        params = {"title": "abc", "content": "abc", "deadline": "2021-06-07"}
        response = self.client.post(self.TASKCREATE_URL, params, format="json")
        params = {"title": "cba", "content": "cba", "deadline": "2021-06-09"}
        response = self.client.post(self.TASKCREATE_URL, params, format="json")
        response = self.client.get(self.TARGET_URL, params, format="json")
        self.assertEqual(response.status_code, 200)
        tasks_queryset = Task.objects.all().values()
        expected_json_dict = [
            {
                "pk": tasks_queryset[0]["id"],
                "title": tasks_queryset[0]["title"],
                "content": tasks_queryset[0]["content"],
                "deadline": tasks_queryset[0]["deadline"].strftime("%Y-%m-%d"),
                "user": {"email": self.user.email, "username": self.user.username},
            },
            {
                "pk": tasks_queryset[1]["id"],
                "title": tasks_queryset[1]["title"],
                "content": tasks_queryset[1]["content"],
                "deadline": tasks_queryset[1]["deadline"].strftime("%Y-%m-%d"),
                "user": {"email": self.user.email, "username": self.user.username},
            },
        ]
        self.assertJSONEqual(response.content, expected_json_dict)

    def test_list_with_other_user(self):

        token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION="JWT " + token)

        params = {"title": "abc", "content": "abc", "deadline": "2021-06-07"}
        response = self.client.post(self.TASKCREATE_URL, params, format="json")

        other_user = get_user_model().objects.create_user(
            email="xxx@example.com", username="abc", password="abc"
        )

        # 違うユーザーがログイン
        token = str(RefreshToken.for_user(other_user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION="JWT " + token)
        response = self.client.get(self.TARGET_URL, params, format="json")
        self.assertEqual(response.status_code, 200)
        expected_json_dict = []
        self.assertJSONEqual(response.content, expected_json_dict)
