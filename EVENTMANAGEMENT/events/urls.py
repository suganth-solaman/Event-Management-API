from django.urls import path
from . import views

urlpatterns = [
    path("api/admin/create/", views.CreateEvent.as_view(), name='create'),
    path("api/admin/list/", views.ListEvents.as_view(), name='list'),
    path("api/admin/update/<int:pk>/", views.UpdateEvent.as_view(), name='update'),
    path("api/admin/view/event/<int:pk>/", views.ViewEventSummery.as_view(), name='viewevent'),
    path("api/user/view/", views.ViewEvents.as_view(), name='view'),
    path("api/user/book/", views.BookEvents.as_view(), name='book'),
    path("api/user/ticket/viewall/", views.ViewAllRegistration.as_view(), name='viewall'),
    path("api/user/ticket/view/<int:pk>/", views.ViewTicket.as_view(), name='viewticket'),
]