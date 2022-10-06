from django.urls import path
from .import views

app_name = 'predict'

urlpatterns = [
    #Here we will just every path we will print
    path('',views.predict,name = 'predict'),
    path('predict/', views.predict_chances, name='submit_prediction'),
    path('results/', views.view_results, name='results'),
    path('about/', views.about, name='about'),
    path('contact/',views.contact, name='contact'),
]