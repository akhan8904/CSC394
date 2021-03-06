from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home', views.index, name="home"),
    url(r'^login',views.loginPage, name="login"),
    url(r'^logout', views.logoutPage, name='logout'),
    url(r'^register',views.register, name="register"),
    url(r'^browse',views.coursecatalog, name="browse"),
    url(r'^plan',views.plan, name="plan"),
    url(r'^about',views.about, name="about"),
    url(r'^account',views.account, name="account"),
]