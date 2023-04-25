from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Post

class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser = User.objects.create_user(username='testuser', password='testpass')
        testuser.save()

        # Create a post
        test_post = Post.objects.create(
            title='Test Post',
            content='Hi, This is a test post',
            author=testuser,
            date_posted=timezone.now(),
        )
        test_post.save()

    def test_title_content(self):
        post = Post.objects.get(id=1)
        expected_title = f'{post.title}'
        expected_content = f'{post.content}'
        self.assertEqual(expected_title, 'Test Post')
        self.assertEqual(expected_content, 'Hi, This is a test post')

    def test_author(self):
        post = Post.objects.get(id=1)
        expected_author = f'{post.author}'
        self.assertEqual(expected_author, 'testuser')

    def test_date_posted(self):
        post = Post.objects.get(id=1)
        expected_date_posted = f'{post.date_posted}'
        self.assertEqual(expected_date_posted, timezone.now().strftime('%Y-%m-%d'))

  
    @classmethod
    def tearDownClass(cls):
        User.objects.all().delete()