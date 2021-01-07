from django.urls import path
from clearning import views
from django.contrib.auth import views as g

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('cnt/',views.contact,name="ct"),
	path('rg/',views.register,name="reg"),
	path('ds/',views.dashboard,name="dsh"),
	path('pf/',views.prfle,name="pfe"),
	path('upf/',views.updf,name="upfe"),
	path('st/',views.start,name="strt"),
	path('Cdatacontrols/',views.cflow,name="cdf"),
	path('fn/',views.fcn,name="func"),
	path('ar/',views.arr,name="arry"),
	path('ptr/',views.poter,name="pointr"),
	path('str/',views.strg,name="string"),
	path('stru/',views.struc,name="struct"),
	path('un/',views.uni,name="unin"),
	path('exa/',views.onlineexam,name="ex"),
	path('lg/',g.LoginView.as_view(template_name="html/login.html"),name="lgn"),
	path('lgg/',g.LogoutView.as_view(template_name="html/logout.html"),name="lgo"),
]