from django.shortcuts import render
from . models import Fitness,Booking
from . serializer import FitnessSerializer,BookingSerializer,BookingRequestSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def list_classes(request):
    fitness_class = Fitness.objects.all()
    serializer = FitnessSerializer(fitness_class,many = True)
    return Response(serializer.data)

@api_view(['POST'])
def book_classes(request):
    serializer = BookingRequestSerializer(data=request.data)
    if serializer.is_valid():
        try:
            fitness_class = Fitness.objects.get(id = serializer.validated_data['class_id'])
        except Fitness.DoesNotExist:
            return Response({"error":"Class Not Found"},status=status.HTTP_404_NOT_FOUND)

        if fitness_class.available_slot <= 0:
            return Response({"error":"No slots available"},status=status.HTTP_400_BAD_REQUEST)

        booking = Booking.objects.create(
            fitness_class = fitness_class,
            client_name = serializer.validated_data['client_name'],
            client_email = serializer.validated_data['client_email']
        )
        fitness_class.available_slot -= 1
        fitness_class.save()
        return Response(BookingSerializer(booking).data,status = status.HTTP_201_CREATED)
    return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
            

@api_view(['GET'])
def get_booking(request):
    email = request.GET.get('email')
    if not email:
        return Response({"error":"Email is required"},status = 400)
    booking = Booking.objects.filter(client_email = email)
    return Response(BookingSerializer(booking,many=True).data)