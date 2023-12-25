from django.urls import path, include

from trf.views import TestingDetailListView, customerTRFView,  testformsetView


urlpatterns = [
    path("trf/testpara/", testformsetView),
    path("trf/<str:trf_code>/", customerTRFView),
    path("trf/tdetail/<str:trf_code>/", TestingDetailListView.as_view()),
]