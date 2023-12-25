from django.urls import path, include

from samples.views import TestParameterListView




urlpatterns = [
    path("tests/<int:product_id>/", TestParameterListView.as_view()),

]