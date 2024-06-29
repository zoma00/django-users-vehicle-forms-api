from rest_framework import serializers
from first_app.models import VehicleType, Client, Service, ServiceVIN, Vehicle  # Import all relevant models
#from rest_framework.renderers import JSONRenderer

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'description')  # Fields to be serialized

class ServiceVINSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceVIN
        fields = ('id', 'vin')  # Fields to be serialized



class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = '__all__' # Fields to be serialized

class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = ('id','type_name','model_name','year','client','purchase_date','color','engine_capacity','service_vin','services')



class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'id', 'first_name', 'last_name', 'email', 'address_line1', 'address_line2',
            'city', 'state', 'postal_code', 'phone_number'
        )








