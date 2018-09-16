from django.conf.urls import url 
from sih_app import views

# TEMPLATE TAGGING
app_name = 'sih_app'

urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
    
]