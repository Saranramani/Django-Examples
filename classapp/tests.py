from django.test import TestCase
from rest_framework.test import APITestCase,APIClient
from .factories import TodoFactory,UserFactory
from .models import TodoClass
from rest_framework import status
from rest_framework.authtoken.models import Token


class AuthentictaionTesting(APITestCase):
    def setUp(self):
        self.user = UserFactory.create()
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

class TodoGetApiTest(APITestCase):
    def setUp(self) -> None:
        TodoFactory.create_batch(2)

    def test_get_endpoint(self):
        url = '/cls/getall/'
        response = self.client.get(url)
        # tododatas = TodoClass.objects.all()
        # expect_data = [{"id":t.id, "todo":t.todo} for t in tododatas]
        # print(expect_data)
        # print(response.data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data, expect_data)

class TodoPostTest(APITestCase):
    def test_post_endpoint(self):
        url = '/cls/add/'
        datas = {"todo":"Helo boy"}
        response = self.client.post(url, datas, format='json')
        print(response.data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

class TodoGetByIdTest(APITestCase):
    def test_getbyid_endpoint(self):
        todo = TodoFactory.create()
        url = f'/cls/getbyid/{todo.id}/'
        tododatas = TodoClass.objects.get(id=todo.id)
        print(tododatas.data)
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

class TodoUpdateApi(APITestCase):
    def test_put_endpoint(self):
        todo = TodoFactory.create()
        url = f'/cls/update/{todo.id}/'
        data = {"id":todo.id,"todo":"Hello boy",}
        response = self.client.put(url, data, format='json')
        print(todo.todo)
        todo.refresh_from_db()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,data)

class TodoDeleteApi(APITestCase):
    def test_delete_endpoint(self):
        todo = TodoFactory.create()
        url = f'/cls/delete/{todo.id}/'
        response = self.client.delete(url, format='json')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

class NotAuthenticate(APITestCase):
    def setUp(self) -> None:
        TodoFactory.create_batch(3)
    
    def test_not_get_auth(self):
        url = '/cls/getall/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class AuthTest(AuthentictaionTesting):
    def test_get_auth(self):
        TodoFactory.create_batch(2)
        url = '/cls/getall/'
        response = self.client.get(url)
        titles = TodoClass.objects.all()
        expected_data = [{"id":t.id,"todos":t.todo}for t in titles]
        print(expected_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class AuthPost(AuthentictaionTesting):
    def test_auth_api(self):
        url = '/cls/add/'
        data = { 'todo':"This is for testing"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class AuthUpdate(AuthentictaionTesting):
     def test_put_endpoint(self):
        todo = TodoFactory.create()
        url = f'/cls/update/{todo.id}/'
        data = {"id":todo.id,"todo":"Hello boy",}
        response = self.client.put(url, data, format='json')
        todo.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class AuthDelete(AuthentictaionTesting):
    def test_auth_api(self):
        todo = TodoFactory.create()
        url = f'/cls/delete/{todo.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)