from django.urls import path
from . import views

urlpatterns = [
    path('' , views.enroll , name='enroll'),
    # path('', include(router.urls))
]