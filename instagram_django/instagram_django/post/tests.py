from django.test import TestCase
from django.db import models
from django.contrib.auth.models import User
import uuid
from authy.views import *

from post.models import Tag,Post

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class PostTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):                                     
        cls.post = Post.objects.create(
            picture="Doe",
            caption='caption',
            user=models.ForeignKey(User,on_delete=models.CASCADE)
        ) 
    
    def test_it_has_information_fields(self):    
        self.assertIsInstance(self.post.caption, str)
        self.assertIsInstance(self.post.picture, str)

class TestAuthProfileUser(TestCase):
    def setUp(self):
        super().setUp()

        self.service = Signup
    def test__register__success(self):
        actual_dto = self.service.register(
            data=UserProfile(
                username="test", email="test@test.com", password="test"
            )
        )

        self.assertEqual(actual_dto.username, "test")
        self.assertIsNotNone(actual_dto.token)

    def test__login__success(self):
        user = User.objects.create_user(
            username="test", email="test@test.com", password="test"
        )

        actual_dto = self.service.login(
            data=SignupForm(
                username=user.username,
                password="test",
            )
        )

        self.assertEqual(actual_dto.username, user.username)