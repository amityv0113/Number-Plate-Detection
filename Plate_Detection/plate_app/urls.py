from django.conf.urls import url
from plate_app import views
from django.conf.urls import include

app_name = 'basic_app'

urlpatterns = [
    url(r'^$',views.algorithm_page , name="algorithm_page"),
    
    url(r'^machine_learing/',views.machine_learing , name ="machine_learing"),
    url(r'^more/' , views.more_page , name ="more"),
    url(r'^register/$' ,views.register,name='register'),
    # url(r'^user_login/$',views.index1,name= "user_login"),
    
]
 