# django imports
from django.urls import path

# relative imports
from .views import TodoApi, TodoRoutes, UserInformationView

urlpatterns = [
    path('todos/', TodoApi.as_view()),
    path('todo/<int:pk>', TodoRoutes.as_view()),
    path('get_user/', UserInformationView.as_view()),
]