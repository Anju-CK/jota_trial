from django.urls import path
from .views import (MatterportSpaceListView,dashboard_view,settings_view,login_view,
                    landing_screen_view,editspace_view,brand_view,whitelabel_view,
                    embed_view,space_view, addspace_view)

urlpatterns = [
    path('', landing_screen_view, name='landing_screen'),
    path('spaces/', MatterportSpaceListView.as_view(), name='space_list'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('settings/', settings_view, name='settings'),
    path('login/', login_view, name='login'),
    path('space/', space_view, name='space'),
    path('editspace/', editspace_view, name='editspace'),
    path('addspace/', addspace_view, name='addspace'),
    path('embed/', embed_view, name='embed'),
    path('brand/', brand_view, name='brand'),
    path('labeling/', whitelabel_view, name='whitelabel'),
]
