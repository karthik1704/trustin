from django.urls import path, include

from trf.views import TestingDetailListView, customerTRFView,  testformsetView, trf_success

app_name = 'trf'

urlpatterns = [
    path("trf/testpara/", testformsetView),
    path("trf/success/", trf_success, name="trf_success"),
    path("trf/<str:trf_code>/", customerTRFView),
    path("trf/tdetail/<str:trf_code>/", TestingDetailListView.as_view()),
]