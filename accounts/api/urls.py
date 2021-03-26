from django.urls import path

from .views import UserList, UserDetail, LoggedInUser

urlpatterns = [
    path('', UserList.as_view()),
    path('<int:pk>/', UserDetail.as_view()),
    path('get_user_info/', LoggedInUser.as_view(), name='logged_in_user')
]