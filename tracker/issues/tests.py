from django.test import TestCase
from rest_framework import status
from .models import Issue


class IssueTestCase(TestCase):

	def test_list(self):
		response = self.client.get(
			'/issues/',
			content_type='application/json',
		)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.json()), 1)

	def test_update(self):
		issue = Issue.objects.create(
			summary='Testing issue update',
			description='Test should update issue successfully',
			type='TASK',
			status=Issue.Status.OPEN
		)

		response = self.client.put('/issues/1/', {
			'summary': issue.summary,
			'description': 'Updated description',
			'type': issue.type,
			'status': issue.status,
		},
			content_type='application/json'
		)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		issue.refresh_from_db()
		response_json = response.json()
		self.assertEqual(response_json['summary'], 'Testing issue update')
		self.assertEqual(response_json['description'], 'Updated description')
		self.assertEqual(response_json['type'], 'TASK')
