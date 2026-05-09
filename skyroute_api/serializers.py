from rest_framework import serializers
from .models import Flight, Airline


class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = ['id', 'name', 'country']


class FlightSerializer(serializers.ModelSerializer):
    airline = AirlineSerializer(read_only=True)
    airline_id = serializers.PrimaryKeyRelatedField(
        queryset=Airline.objects.all(),
        write_only=True,
        source='airline'
    )

    class Meta:
        model = Flight
        fields = ['id', 'code', 'origin', 'destination', 'airline', 'airline_id']