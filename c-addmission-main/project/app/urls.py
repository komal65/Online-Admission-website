from django.urls import path,include
from . import views
urlpatterns = [
    path("home/" , views.HomePage,name="home"),
    path("" , views.SignupPage,name="Signup"),
    path("register/" , views.RegisterUser,name='register'),
    path("otppage/" , views.OtpPage,name='otppage'),
    path("otp/" , views.OtpVerify , name = 'otp'),
    path("loginpage/" , views.LoginPage , name = 'loginpage'),
    path("loginuser/" , views.LoginUser, name = 'login'),
    path("admission/" , views.AdmissionPage, name = 'admission'),
    path("updateprofile/" , views.UpdateProfile, name = 'updateprofile'),
    path("aboutus/" , views.AboutusPage, name= 'aboutus'),
    path("undertaking/" , views.UnderTakingPage, name= 'undertaking'),
    path("undername/" , views.Undertaking_name, name= 'undertaking_name'),
    path("document/" , views.DocUpload, name= 'document')


    



]