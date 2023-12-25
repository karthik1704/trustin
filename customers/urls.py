from django.urls import path, include

from customers.views import CustomerRetrieveView


urlpatterns = [
    path("retrieve/<int:pk>/", CustomerRetrieveView.as_view()),

]