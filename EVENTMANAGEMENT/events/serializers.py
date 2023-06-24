from rest_framework import serializers
from .models import EventDetails
from django.contrib.auth.models import User
from datetime import datetime, date

from .models import EventDetails, Tickets


class EventDetailsCreate(serializers.ModelSerializer):
    class Meta:
        model = EventDetails
        fields = ('event', 'start_date', 'end_date', 'seat', 'details')

    def validate(self, data):
        required_fields = ['event', 'start_date', 'end_date', 'seat']

        for field in required_fields:
            if field not in data or data[field] is None:
                raise serializers.ValidationError(f"The '{field}' field is required.")

        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class ListEvent(serializers.ModelSerializer):
    class Meta:
        model = EventDetails
        fields = ('event', 'start_date', 'end_date', 'seat')


class UpdateSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        if 'event' in validated_data:
            instance.event = validated_data['event']
        if 'start_date' in validated_data:
            instance.start_date = validated_data['start_date']
        if 'end_date' in validated_data:
            instance.end_date = validated_data['end_date']
        if 'seat' in validated_data:
            instance.seat = validated_data['seat']
        if 'details' in validated_data:
            instance.details = validated_data['details']

        instance.save()
        return instance

    class Meta:
        model = EventDetails
        fields = ('event', 'start_date', 'end_date', 'seat', 'details')


class BookingSerializer(serializers.ModelSerializer):

    def validate(self, data):
        required_fields = ['event', 'date', 'seats']

        for field in required_fields:
            if field not in data or data[field] is None:
                raise serializers.ValidationError(f"The '{field}' field is required.")
        if data['event'].start_date <= data["date"] <= data['event'].end_date:
            pass
        else:
            raise serializers.ValidationError(f"The Date should be between {data['event'].start_date} - "
                                              f"{data['event'].end_date} these two dates.")
        if 0 < data["seats"] <= data['event'].seat:
            pass
        else:
            raise serializers.ValidationError(f"The Date should be between 1 - "
                                              f"{data['event'].seat}")

        return data

    def create(self, validated_data):
        seat = validated_data.pop('seats')
        query_set = EventDetails.objects.get(id=validated_data['event'].id)
        query_set.seat -= seat
        query_set.save()
        book, created = Tickets.objects.get_or_create(**validated_data)
        if book.seats:
            book.seats += seat
        else:
            book.seats = seat
        book.save()

        return book

    class Meta:
        model = Tickets
        fields = ('event', 'date', 'seats')
