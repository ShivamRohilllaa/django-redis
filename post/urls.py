from django.urls import path
from post.views import home
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('set-cache', views.set_data_in_cache, name='set-redis-data'),
    path('get-cache', views.get_data_from_cache, name='get-redis-data'),

]
