from django.test import TestCase
from .models import User, Post

class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', password='password')
        self.post = Post.objects.create(content='This is a test post', author=self.user)

    def test_post_creation(self):
        self.assertEqual(self.post.content, 'This is a test post')
        self.assertEqual(self.post.author.username, 'testuser')
