from django.urls import path
urlpatterns = [
    path('',views.hello),
    path('acerca/',views.about)
]