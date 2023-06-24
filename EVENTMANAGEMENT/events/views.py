#builtin modules
from rest_framework.permissions import IsAdminUser
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

#user defined Modules
from .serializers import EventDetailsCreate, UserSerializer, ListEvent, UpdateSerializer, BookingSerializer
from .models import EventDetails, Tickets


@method_decorator(csrf_exempt, name='dispatch')
class CreateEvent(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]
    serializer_class = UserSerializer

    def post(self, request):
        responses = {"message": "Success!", "details": '', "status": 1}
        serializer = EventDetailsCreate(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        responses["details"] = [serializer.data]
        return Response(responses, status=status.HTTP_201_CREATED)


@method_decorator(csrf_exempt, name='dispatch')
class ListEvents(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]
    serializer_class = ListEvent

    def post(self, request):
        responses = {"message": "Success!", "details": '', "status": 1}
        query_set = EventDetails.objects.filter(user__id=request.user.id).values()
        responses["details"] = query_set
        return Response(responses, status=status.HTTP_200_OK)


@method_decorator(csrf_exempt, name='dispatch')
class UpdateEvent(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]
    serializer_class = UpdateSerializer

    def post(self, request, pk):
        responses = {"message": "Success!", "details": '', "status": 1}
        query_set = EventDetails.objects.get(id=pk)
        serializer = UpdateSerializer(query_set, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        responses["details"] = serializer.data
        return Response(responses, status=status.HTTP_200_OK)


@method_decorator(csrf_exempt, name='dispatch')
class ViewEventSummery(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

    def post(self, request, pk):
        responses = {"message": "Success!", "details": '', "status": 1}
        query_set = EventDetails.objects.filter(id=pk).values()
        responses["details"] = list(query_set)
        return Response(responses, status=status.HTTP_200_OK)


class ViewEvents(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        responses = {"message": "Success!", "details": '', "status": 1}
        query_set = EventDetails.objects.all().values()
        responses["details"] = list(query_set)
        return Response(responses, status=status.HTTP_200_OK)


class BookEvents(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        responses = {"message": "Success!", "details": '', "status": 1}
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        responses["details"] = serializer.data
        return Response(responses, status=status.HTTP_200_OK)


class ViewAllRegistration(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        responses = {"message": "Success!", "details": '', "status": 1}
        query_set = Tickets.objects.filter(user=request.user).order_by('date').values('id', 'event__event', 'date', 'seats')
        responses["details"] = query_set
        return Response(responses, status=status.HTTP_200_OK)


class ViewTicket(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        responses = {"message": "Success!", "details": '', "status": 1}
        query_set = Tickets.objects.filter(id=pk, user=request.user).order_by('date').values('id', 'event__event', 'date', 'seats')
        responses["details"] = query_set
        return Response(responses, status=status.HTTP_200_OK)


