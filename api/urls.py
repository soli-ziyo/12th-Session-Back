from django.urls import path
from api.views import SignUpView, LoginView

app_name= 'api'

urlpatterns= [
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
]