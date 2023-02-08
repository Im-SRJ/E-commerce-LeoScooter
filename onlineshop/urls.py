from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('careers/', views.careers,name='careers'),
    path('contact/', views.contact,name='contact'),
    path('hasten/', views.hasten,name='hasten'),
    path('testdrive/', views.testdrive,name='testdrive'),
    path('add_to_cart/', views.cart,name='add_to_cart'),
    path('cart/', views.showcart,name='cart'),
    path('checkout/', views.checkout,name='checkout'),
    path('paymentdone/', views.paymentdone,name='paymentdone'),
    path('handlerequest/', views.handlerequest,name='handlerequest'),
    path('orders/', views.orders,name='orders'),
    path('h5/', views.h5,name='h5'),
    # path('profile/', views.profile,name='profile'),
    path('address/', views.address,name='address'),
    path('profile/', views.profileview.as_view(),name='profile'),
    path('register/', views.register,name='register'),
    # path('registration/', views.CustomerRegistrationView.as_view(),name='registeration'),
    path('userlogin/', views.userlogin,name='userlogin'),
    path('logout/', views.logout,name='logout'),
    path('base/', views.base,name='base'),
    path('productdetails/<int:id>/', views.productdetails,name='productdetails'),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),
]