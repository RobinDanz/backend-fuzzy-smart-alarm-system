from django.test import TestCase

class HelloTestCase(TestCase):
    def setUp(self) -> None:
        pass

    def test_hello_world(self):
        print('hello world')
        self.assertTrue(True)
