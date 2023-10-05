from django.contrib import admin
from django.urls import path
from cream.views import createLarek,home,createCream

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name="home-page"),
    path('create-larek',createLarek.as_view(),name='create-larek'),
    path('create-cream',createCream.as_view(),name='create-cream')
]
