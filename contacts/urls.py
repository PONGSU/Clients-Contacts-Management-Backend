from django.urls import path
from contacts.views import ContactListView, ContactCreateView, ContactDetailsView

urlpatterns = [
    path("contacts/", ContactListView.as_view()),
    path("contacts/register/", ContactCreateView.as_view()),
    path("contacts/<int:pk>/", ContactDetailsView.as_view()),
]
