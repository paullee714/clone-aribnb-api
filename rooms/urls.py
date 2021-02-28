from django.urls import path
from . import views

app_name = "rooms"

urlpatterns = [
    # path("list/", views.ListRoomsView.as_view()),
    # path("list/", views.rooms_view),
    path("list/",views.RoomsView.as_view()),
    path('<int:pk>/',views.RoomView.as_view()),
    path('search/',views.room_search)
]
