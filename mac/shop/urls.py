from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name="shopHome"),
    path("about/",views.about,name="AboutUs"),
    path("contact/",views.contact,name="ContactUs"),
    path("search/",views.search,name="Search"),
    path("tracker/",views.tracker,name="Tracker"),
    path("productview",views.productView,name="ProductView"),
    path("checkout",views.checkout,name="Checkout"),
]