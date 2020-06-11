from django.test import TestCase
from .models import Messages
class PostModelTest(TestCase):
    def setUp(self):
        Messages.objects.create(text='just a test')
    def test_text_content(self):
        post=Messages.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')