from mock import Mock





class MockClientAPI:
    def __init__(self):
        self.clients_data  = [
    {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@example.com",
        "address_line1": "123 Main St",
        "address_line2": "Apt. B",
        "city": "Anytown",
        "state": "CA",
        "postal_code": "12345",
        "phone_number": "+15551234567",
    },
    {
        "id": 2,
        "first_name": "Jane",
        "last_name": "Smith",
        "email": "janesmith@example.com",
        "address_line1": "456 Elm St",
        "city": "Springfield",
        "state": "NY",
        "postal_code": "54321",
    },
]

    def get_client(self, pk):
        for client in self.clients_data:
            if client['id'] == pk:
                return client
        return None

    def create_client(self, data):
        # Simulate creation logic and return mock data
        new_client_id = max(client['id'] for client in self.clients_data) + 1
        new_client = {'id': new_client_id, **data}
        self.clients_data.append(new_client)
        return ClientSerializer(new_client).data

vehicle_types_data = [
    {"id": 1, "type_name": "Car"},
    {"id": 2, "type_name": "Truck"},
]

vehicles_data = [
    {
        "id": 1,
        "type_name": 1,  # Foreign key reference to vehicle_types_data
        "model_name": "Camry",
        "year": 2020,
        "client": 1,  # Foreign key reference to clients_data
        "purchase_date": "2020-01-01",
        "color": "Silver",
        "engine_capacity": 2500,
    },
    {
        "id": 2,
        "type_name": 2,  # Foreign key reference to vehicle_types_data
        "model_name": "F-150",
        "year": 2022,
        "client": None,  # Client can be null
        "purchase_date": None,
        "color": "Red",
        "engine_capacity": 3500,
    },
]


def get_clients(url):
    #Mock function to retrieve client data.
    if url == "/clients/":
        return clients_data
    else:
        # Simulate handling specific client detail retrieval by ID
        client_id = url.split("/")[-2]
        for client in clients_data:
            if str(client["id"]) == client_id:
                return client
        return None  # Return None for non-existent client


def get_vehicle_types(url):
    #Mock function to retrieve vehicle type data.
    if url == "/vehicle_types/":
        return vehicle_types_data
    else:
        # Simulate handling specific vehicle type detail retrieval by ID
        vehicle_type_id = url.split("/")[-2]
        for vehicle_type in vehicle_types_data:
            if str(vehicle_type["id"]) == vehicle_type_id:
                return vehicle_type
        return None  # Return None for non-existent vehicle type


def get_vehicles(url):
    """Mock function to retrieve vehicle data."""
    if url == "/vehicles/":
        return vehicles_data
    else:
        # Simulate handling specific vehicle detail retrieval by ID
        vehicle_id = url.split("/")[-2]
        for vehicle in vehicles_data:
            if str(vehicle["id"]) == vehicle_id:
                return vehicle
        return None  # Return None for non-existent vehicle


# Add more mock functions (e.g., for posting data) as needed
