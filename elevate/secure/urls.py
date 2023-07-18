from django.urls import path

from . views import SafetyCheckView

urlpatterns = [
    path('safety-check/', SafetyCheckView.as_view(), name='safety_check'),
]
