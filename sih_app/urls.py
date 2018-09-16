from django.conf.urls import url 
from sih_app import views

# TEMPLATE TAGGING
app_name = 'sih_app'

urlpatterns = [
    url(r'^users/$',views.users,name='users'),
    # url(r'^other/$',views.other,name='other'),
    
]