# from django.test import TestCase
# from rest_framework import status
# from rest_framework.test import APITestCase
# from .models import Item
# from .factries import ItemFactory

# class TodosTest(APITestCase):
#     def setUp(self) -> None:
#         ItemFactory.create_batch(2)
    
#     def test_get_todo(self):
#         url = '/api/getall/'
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
    
#     def test_get_todo(self):
#         todo = ItemFactory.create()
#         url = f'/api/getbyid/{todo.id}/'
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
    
#     def test_create_todo(self):
#         url = '/api/add/'
#         data = {"name":"Welcome to E2"}
#         response = self.client.post(url, data, fromat='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_update_todo(self):
#         todo = ItemFactory.create()
#         url = f'/api/update/{todo.id}/'
#         data = {"name":"sangeetha"}
#         response = self.client.put(url, data, fromat='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
    
#     def test_delete_todo(self):
#         todo = ItemFactory.create()
#         url = f'/api/delete/{todo.id}/'
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)