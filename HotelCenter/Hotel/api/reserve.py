import http

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.utils.timezone import datetime
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from ..filter_backends import *
from ..permissions import *
from ..models import Reserve, Room, RoomSpace
from ..serializers.reserve_serializers import RoomReserveSerializer, ReserveSerializer


class RoomspaceReserveList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, roomspace_id, format=None):
        roomspace = get_object_or_404(RoomSpace, id=roomspace_id)
        hotel = roomspace.room.hotel
        reserveList = Reserve.objects.filter(roomspace=roomspace)
        if (not request.user == hotel.creator) and (not request.user in hotel.editors.all()):
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = RoomReserveSerializer(reserveList, many=True)
        return Response(serializer.data, status=http.HTTPStatus.OK)


class ReserveList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        reserveList = Reserve.objects.filter(user=request.user)
        serializer = ReserveSerializer(reserveList, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        room_id = request.data['room']
        room = get_object_or_404(Room, id=room_id)
        roomspace_list = RoomSpace.objects.filter(room=room).all()
        serializer = ReserveSerializer(data=request.data)
        if serializer.is_valid():
            today = datetime.today()
            if (today.date() > serializer.validated_data["start_day"] or serializer.validated_data["start_day"] >
                    serializer.validated_data["end_day"]):
                return Response('dates not valid', status=status.HTTP_403_FORBIDDEN)
            if (request.user.balance < (
                    (serializer.validated_data["end_day"] - serializer.validated_data["start_day"]).days + 1) *
                    serializer.validated_data["price_per_day"]):
                return Response(data='credit Not enough', status=status.HTTP_406_NOT_ACCEPTABLE)
            for roomspace in roomspace_list:
                if (checkCondition(roomspace, serializer.validated_data["start_day"],
                                   serializer.validated_data["end_day"])):
                    serializer.save(user=user, roomspace=roomspace)
                    user.balance -= ((serializer.validated_data["end_day"] - serializer.validated_data[
                        "start_day"]).days + 1) * serializer.validated_data["price_per_day"]
                    user.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def checkCondition(roomspace, start, end):
    roomspace_reserve_list = Reserve.objects.filter(roomspace=roomspace).all()
    for roomspace_reserve in roomspace_reserve_list:
        if ((roomspace_reserve.start_day <= start <= roomspace_reserve.end_day) or (
                roomspace_reserve.start_day <= end <= roomspace_reserve.end_day)):
            return False
    return True


class AdminReserveViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend]
    permission_classes = (IsAuthenticated, IsReserveHotelEditor)
    filterset_class = AdminReserveFilter
    serializer_class = ReserveSerializer

    def get_queryset(self):
        query_set = Reserve.objects.filter(room__hotel=self.kwargs.get('hid')).all()
        return query_set

