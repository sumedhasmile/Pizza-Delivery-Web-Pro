
from django.urls import path
from .views import declineorder,acceptorder,adminorders,userorders,placeorder,userlogout,userauthenticate,customerwelcomeview,userloginview,adminloginview,signupuser,adminhomepageview,authenticateadmin,logoutadmin,addpizza,deletepizza,homepageview

urlpatterns = [
    path("admin1/",adminloginview, name='adminloginpage'),
    path("adminauthenticate/", authenticateadmin),
    path("admin/homepage/", adminhomepageview, name= 'adminhomepage'),
    path("admin/logout/",logoutadmin ),
    path("addpizza/", addpizza),
    path("deletepizza/<int:pizzaid>/",deletepizza),
    path("",homepageview , name= 'homepage'),
    path("signupuser/", signupuser),
    path('loginuser/',userloginview, name= 'userloginpage'),
    path('customerwelcome/',customerwelcomeview , name= 'customerpage'),
    path('customerauthenticate/', userauthenticate),
    path('userlogout/',userlogout),
    path("placeorder/", placeorder),
    path("userorders/", userorders),
    path("adminorders/", adminorders),
    path("acceptorder/<int:orderpk>/", acceptorder),
    path("declineorder/<int:orderpk>/",declineorder)
]