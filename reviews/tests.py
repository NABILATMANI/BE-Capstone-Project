from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class MovieReviewTests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Obtain JWT token
        url = reverse('token_obtain_pair')
        response = self.client.post(url, {'username': 'testuser', 'password': 'testpass'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Save the access token for future requests
        self.access_token = response.data['access']

    def test_create_review(self):
        url = reverse('moviereview-list')  # Assuming 'moviereview-list' is the view name
        data = {
            "movie_title": "Interstellar",
            "review_content": "Incredible movie!",
            "rating": 5
        }
        # Set the Authorization header with the token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        # Send the POST request
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response.data)  # Optional: See the response data for debugging
