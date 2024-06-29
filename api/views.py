from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.decorators import api_view  # Corrected import
from rest_framework.permissions import IsAuthenticated  # Optional for access control
from django.contrib.auth import authenticate, login  # For user login
from rest_framework.views import APIView  # Added import
from accounts.utils.token import generate_manual_token
from first_pro.mock_api import get_clients, get_vehicle_types, get_vehicles

from first_app.models import VehicleType, Client, Vehicle, ServiceVIN, Service
from .serializers import (
    VehicleTypeSerializer,
    ClientSerializer,
    ServiceVINSerializer,
    ServiceSerializer,
    VehicleSerializer
)



class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    permission_classes = [IsAuthenticated]

# ... similar viewsets for other models

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]  # Optional for access control

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mock_api = MockClientAPI()

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]

class PurchasedClientsView(APIView):
    permission_classes = [IsAuthenticated]  # Optional for access control

    def get(self, request):
        purchased_clients = Client.objects.order_by("first_name")
        serializer = ClientSerializer(purchased_clients, many=True)
        return Response(serializer.data)



@api_view(['POST'])
def login_api(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if user is None:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    login(request, user)  # Log the user in

    # Remove token creation logic (as discussed earlier)

    return Response({'message': 'Login successful'})

