from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='main'),
    path('video_view/<slug:video_slug>/',views.video_view,name='video_player'),
    path('posting/',views.posting,name='posting_page')
]