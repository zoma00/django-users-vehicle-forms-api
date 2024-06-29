from django.core.wsgi import get_wsgi_application
import os

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_pro.settings')  # Replace 'first_pro' with your project name if it's different

# Get the Django application
from ..wsgi import get_wsgi_application  # Assuming test_endpoint_test.py is in first_app/tests
application = get_wsgi_application()

# Now you can import from Django modules
from rest_framework.test import APIRequestFactory, force_authenticate
# ... rest of your test code
from first_app.models import Client  # Replace with your model name
from api.views import ClientViewSet  # Replace with your actual view name (not PurchasedClientsView)
from .settings import  APIRequestFactory, force_authenticate

class ClientViewSetTest(TestCase):
    def test_get_clients_authenticated(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='Hazem-Adel')  # Replace with actual user

        # Create an unauthenticated request
        request = factory.get('/clients/')

        # Force authentication on the request
        force_authenticate(request, user=user)

        # Call the viewset with the authenticated request
        viewset = ClientViewSet.as_view()  # Create a view instance
        response = viewset(request)  # Call the viewset method

        self.assertEqual(response.status_code, 200)  # Assert successful response
        # Optional assertions on response content


"""
from django.test import Client
from .models import Vehicle

# Create a test client
client = Client()

# Send a GET request to the vehicle endpoint
response = client.get('/api/vehicle/')

# Check the response status code (expected to be 200 for success)
if response.status_code == 200:
    # Response is successfully retrieved, access the content
    rendered_content = response.content
    print(rendered_content)  # This will display the rendered JSON data
else:
    print(f"Error retrieving vehicles: {response.status_code}")
"""

