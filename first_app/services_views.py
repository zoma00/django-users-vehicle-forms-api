from django.shortcuts import render
from first_app.models import Vehicle,Client

def vehicle_list_with_service(request):
    vehicles = Vehicle.objects.prefetch_related('services')  # Prefetch services and client
    vehicles_dict = {'vehicles': vehicles}
    return render(request, 'first_app/service.html', context=vehicles_dict)

