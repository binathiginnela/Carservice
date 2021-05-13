from django.urls import path
from service import views
from django.contrib.auth import views as ad

urlpatterns=[
       path('',views.home,name="home"),
       path('a/',views.about,name="ab"),
       path('c/',views.contact,name="cn"),
       path('log/',ad.LoginView.as_view(template_name="services/login.html"),name="lg"),
       path('reg/',views.registration,name="reg"),
       path('ser/',views.Service,name="ser"),
       path('logout/',ad.LogoutView.as_view(template_name="services/logout.html"),name="lgo"),
       path('profile/',views.profile,name='pro'),
       path('role/',views.role,name="ro"),
       path('e/<int:si>/',views.userupdate,name="ue"),
       path('delt/<int:st>/',views.deletedata,name="delete"),
       path('showdata/',views.showinfo,name="show"),
       path('infodelete/<int:et>',views.infodelete,name='infodelete'),
       path('ch/',views.cgf,name="cg"),
       path('upr/',views.updprofile,name="upf"),
       path('ds/',views.dashboard,name="dsh"),
       path('pro/',views.profile,name="pf"),
       path('reu/',views.booking,name="booking"),
       path('rst/',ad.PasswordResetView.as_view(template_name="services/resetpassword.html"),name="rt"),
       path('rst_done/',ad.PasswordResetDoneView.as_view(template_name="services/resetpassworddone.html"),name="password_reset_done"),
       path('rst_cf/<uidb64>/<token>/',ad.PasswordResetConfirmView.as_view(template_name="services/reset_password_confirm.html"),name="password_reset_confirm"),
       path('rst_cmplt/',ad.PasswordResetCompleteView.as_view(template_name="services/reset_password_complete.html"),name="password_reset_complete"),
       path('viewuser/',views.viewuser,name="viewuser"),
       path('customer/<int:id>/',views.customer,name="customer"),
       path('owner/<int:id>/',views.owner,name="owner"),
       path('ca/<int:id>/',views.categories,name="ca"),
       path('category/',views.addcategory,name="addcategory"),
       path('carservices/',views.addcarservices,name="addcarservices"),
       path('adc/<int:id>/',views.cart,name="act"),
       path('addcart/<int:id>/',views.addcart,name="addcart"),
       path('cartdetails/',views.cartdetails,name="cartdetails"),
       path('placeorder/',views.placeorder,name="placeorder"),
      
]
