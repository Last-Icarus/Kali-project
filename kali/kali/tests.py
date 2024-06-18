from django.test import TestCase
from .models import User, Art, Commission

class AccessabiltyTest(TestCase):
    def test_url(self):
        print('Тест на доступность основных страниц сайта')
        print('Создание пользователей')
        User.objects.create(username='TestUser')
        User.objects.create(username='TestUser_2')

        urls = ['', '/commissions/', '/profile/1', '/profile/2']
        print('Проверка доступности')
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
        print('OK')
        print()


class CreateArtTest(TestCase):  
    def test_create_art(self):
        print('Тест на создание художественной работы')
        print('Создание пользователя')
        author = User.objects.create(username='TestUser_3')
        postres = {'art_name' : 'test',
                   'description' : 'test_text'}
        print('Создание работы')
        Art.objects.create(name=postres['art_name'],
                description=postres['description'],
                likes = 0,
                author=author)
        
        self.assertTrue(Art.objects.filter(name = 'test').exists())
        print('OK')
        print()       
        
class CreateCommissionTest(TestCase):  
    def test_commission_art(self):
        print('Тест на создание предложения')
        print('Создание пользователей')
        author = User.objects.create(username='TestUser_4')
        owner = User.objects.create(username='TestUser_5')
        postres = {'commission_name' : 'test',
                   'description' : 'test_text'}
        
        print('Создание предложения')
        Commission.objects.create(name=postres['commission_name'],
                description=postres['description'],
                likes = 0,
                price= 100,
                author=author,
                owner=owner)
        
        self.assertTrue(Commission.objects.filter(name = 'test').exists())
        print('OK')
        print()

class ContentTest(TestCase):
    def test_main_page_content(self):
        print('Тест на корректность содержания главной страницы')
        print('Получение ответа')
        response = self.client.get('')
        print('Проверка содержания')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Сортировка', response.content.decode())
        self.assertIn('Категории', response.content.decode())
        self.assertIn('Жанр', response.content.decode())
        print('OK')
        print()

