from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from datetime import date, timedelta
from tasks_app.models import Family, Task

class TaskApiTestCase(TestCase):        
    def setUp(self):

        self.client = APIClient()
        self.family = Family.objects.create(name="TestApi")

        self.task_data = {
            "family": self.family.id,
            "title": "Test Task API",
            "description": "This task is used as test for the API",
            "state": "todo",
            "due_date": (date.today() + timedelta(days=5)).isoformat()
        }

    def test_list_tasks(self):
        response = self.client.get('/api/tasks-list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_task_details(self):
        self.task_data['family'] = self.family
        task = Task.objects.create(**self.task_data)
        response = self.client.get(f'/api/task-detail/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task_success(self):
        response = self.client.post('/api/task-detail/create-task/', self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_task_due_date_past(self):
        self.task_data["due_date"] = (date.today() - timedelta(days=1)).isoformat()
        response = self.client.post('/api/task-detail/create-task/', self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_invalid_state(self):
        self.task_data['family'] = self.family
        task = Task.objects.create(**self.task_data)
        response = self.client.put(f'/api/task-detail/{task.id}/update/', {"state": "invalido"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_task(self):
        self.task_data['family'] = self.family
        task = Task.objects.create(**self.task_data)
        response = self.client.delete(f'/api/task-detail/{task.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



