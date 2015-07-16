from django.test import TestCase, Client

class LessonOneTests(TestCase):

    def test_hello_melbdjango(self):
        c = Client()
        response = c.get('/?name=melbdjango')
        self.assertTrue('melbdjango' in str(response.content))
