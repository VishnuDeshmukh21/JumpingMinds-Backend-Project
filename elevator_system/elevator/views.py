# elevator_system/elevator/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Elevator, Request
from .serializers import ElevatorSerializer, RequestSerializer

class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    # Endpoint to mark an elevator as not working or in maintenance
    @action(detail=True, methods=['post'])
    def mark_maintenance(self, request, pk=None):
        elevator = self.get_object()
        elevator.in_maintenance = True
        elevator.save()
        return Response({'detail': 'Elevator marked as in maintenance'}, status=status.HTTP_200_OK)

    # Endpoint to open the elevator door
    @action(detail=True, methods=['post'])
    def open_door(self, request, pk=None):
        elevator = self.get_object()
        # Your logic for opening the door
        return Response({'detail': 'Door opened'}, status=status.HTTP_200_OK)

    # Endpoint to close the elevator door
    @action(detail=True, methods=['post'])
    def close_door(self, request, pk=None):
        elevator = self.get_object()
        # Your logic for closing the door
        return Response({'detail': 'Door closed'}, status=status.HTTP_200_OK)

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    # Endpoint to fetch all requests for a given elevator
    @action(detail=True, methods=['get'])
    def elevator_requests(self, request, pk=None):
        elevator = Elevator.objects.get(pk=pk)
        requests = elevator.requests.all()
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Endpoint to fetch the next destination floor for a given elevator
    @action(detail=True, methods=['get'])
    def next_destination(self, request, pk=None):
        elevator = Elevator.objects.get(pk=pk)
        # Your logic to determine the next destination floor
        next_floor = 2  # Replace this with your logic
        return Response({'next_destination': next_floor}, status=status.HTTP_200_OK)

    # Endpoint to fetch if the elevator is moving up or down currently
    @action(detail=True, methods=['get'])
    def is_moving(self, request, pk=None):
        elevator = Elevator.objects.get(pk=pk)
        return Response({'moving_up': elevator.moving_up}, status=status.HTTP_200_OK)

    # Endpoint to save user request to the list of requests for an elevator
    @action(detail=True, methods=['post'])
    def save_request(self, request, pk=None):
        elevator = Elevator.objects.get(pk=pk)
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(elevators=[elevator])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


