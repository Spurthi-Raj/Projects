from django.db.models import fields
from . models import Fitness,Booking
from rest_framework import serializers

class FitnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fitness
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class BookingRequestSerializer(serializers.Serializer):
    class_id = serializers.IntegerField()
    client_name = serializers.CharField()
    client_email = serializers.EmailField()