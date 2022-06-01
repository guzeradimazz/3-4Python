from django.test import Client
from django.test import TestCase
from selenium.webdriver import WebDriver


class TestAuthy(TestCase):
    def setUp(self):
        self.client = Client()
    def test_details_posts(self):
        # Issue a GET request.
        response = self.client.get('/user/login/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 posts.
        self.assertEqual(len(response.context['posts']), 5)
    
    def test_details(self):
        client = Client()
        response = client.get('/user/login/')
        self.assertEqual(response.status_code, 200)


    def test_index(self):
        client = Client()
        # Check index.html
        response = client.get('/index/')
        self.assertEqual(response.status_code, 200)
        with self.assertTemplateUsed('index.html'):
            client.get('index.html')
        with self.assertTemplateUsed(template_name='index.html'):
            client.get('index.html')

    def test_logout(self):
        client = Client()
        response = client.get('/user/logout')
        self.assertEqual(response.status_code, 200)

    def test_login(self):

        response = self.client.get('/index/')
        self.assertRedirects(response, '/user/login/?next=/user{0}/')

        with self.settings(LOGIN_URL='/user/login/'):
            response = self.client.get('/index/')
            self.assertRedirects(response, '/other/login/?next=/user{0}/')

class TestLogin(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(cls).setUpClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self, '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('myuser')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('secret')
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()