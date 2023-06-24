from django.db import models
from django.contrib.auth.models import User


class EventDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    event = models.CharField(max_length=100, blank=True,  null=True)
    start_date = models.DateField(default=None, blank=True,  null=True)
    end_date = models.DateField(default=None, blank=True,  null=True)
    seat = models.IntegerField(default=None, blank=True,  null=True)
    details = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.event


class Tickets(models.Model):
    event = models.ForeignKey(EventDetails, on_delete=models.CASCADE, default=None, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    date = models.DateField(default=None, blank=True,  null=True)
    seats = models.IntegerField(default=None, blank=True,  null=True)

    def __str__(self):
        return self.user