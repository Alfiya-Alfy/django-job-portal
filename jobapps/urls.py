from django.urls import path
from .views import landing_page, signup_page, login_page

urlpatterns = [
    path('', landing_page, name='landing_page'),   # root landing page
    path('signup/', signup_page, name='signup_page'),
    path('login/', login_page, name='login_page'),
]
