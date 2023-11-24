from django.contrib.auth.models import User
from django.test import TestCase
from ..models import *
from django.utils.text import slugify
from http import HTTPStatus
from users.context_processors import menu

class LogicTestCaseIndex(TestCase):
    """Тести для головної сторінки index"""

    fixtures = ['women_app_data.json']



    def setUp(self):
        self.posts_test = Women.objects.all()


    def test_post_has_slug(self):
        category_sportsmenki = Category.objects.create(name='Спортсменки')
        user = User(username='John Doe')
        user.save()
        women = Women.objects.create(title='Miroslava',
                                     content='test',
                                     is_published=Women.Status.PUBLISHED,
                                     cat=category_sportsmenki,
                                     )
        women.author = user
        women.save()
        self.assertEqual(women.slug, slugify(women.title))



    def test_women_home(self):
        """Тест сторінки index"""
        path = reverse('home')
        response = self.client.get(path)

        self.__common_tests(response)
        self.assertEqual(response.context_data['title'], 'Головна сторінка')
        self.assertTemplateUsed(response, 'women_app/index.html')


        # Відображення постів на головній сторінці
        self.assertEqual(list(response.context_data['posts']), list(self.posts_test))
        # Відображення головного меню
        self.assertEqual(response.context_data['menu'][:3], menu)



    def test_list_with_categories_aktorki(self):
        """Тест відображення категорії АКТОРКИ"""
        category_test = Category.objects.first()
        posts_test = Women.objects.all()
        path = reverse('category', kwargs={'cat_slug': category_test.slug})
        response = self.client.get(path)



        self.__common_tests(response)
        self.assertTemplateUsed(response, 'women_app/list_categories.html')

        # перевірка на відображення записів з категорією АКТОРКИ
        self.assertEqual(list(response.context_data['posts']),
                         list(posts_test.filter(cat__slug=category_test.slug)))


    def test_list_with_categories_spivachki(self):
        """Тест відображення категорії Співачки"""
        category_test = Category.objects.last()
        path = reverse('category', kwargs={'cat_slug': category_test.slug})
        response = self.client.get(path)


        self.__common_tests(response)
        self.assertTemplateUsed(response, 'women_app/list_categories.html')
        # перевірка на відображення записів з категорією СПІВАЧКИ
        self.assertEqual(list(response.context_data['posts']),
                         list(self.posts_test.filter(cat__slug=category_test.slug)))

    def test_list_tags(self):
        tags = TagPost.objects.first()
        path = reverse('tag', kwargs={'tag_slug': tags.slug})
        response = self.client.get(path)

        self.__common_tests(response)
        self.assertTemplateUsed(response, 'women_app/index.html')
        # перевірка виводі постів з тегом БЛОНДИНКИ
        self.assertEqual(list(response.context_data['posts']),
                         list(self.posts_test.filter(tags__slug=tags.slug)))

    def __common_tests(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['menu'][:3], menu)




class LogicTestCaseAddPageForm(TestCase):
    pass




