from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import Flight, Airline
from .serializers import FlightSerializer, AirlineSerializer


class AirlineViewSet(viewsets.ModelViewSet):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer


class FlightViewSet(viewsets.ModelViewSet):
    serializer_class = FlightSerializer
    filter_backends = [SearchFilter]
    search_fields = ['code', 'origin', 'destination', 'airline__name']

    def get_queryset(self):
        queryset = Flight.objects.all()

        origin = self.request.query_params.get('origin')
        if origin:
            queryset = queryset.filter(origin__icontains=origin)

        destination = self.request.query_params.get('destination')
        if destination:
            queryset = queryset.filter(destination__icontains=destination)

        airline_id = self.request.query_params.get('airline')
        if airline_id:
            queryset = queryset.filter(airline__id=airline_id)

        return queryset