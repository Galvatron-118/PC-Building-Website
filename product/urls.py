from django.urls import path
from . import views

urlpatterns = [
	
    path('cpu/',views.home_view),
    path('motherboard/',views.motherboard_view),
    path('cpucooler/',views.cpucooler_view),
    path('case/',views.case_view),
    path('memory/',views.memory_view),
    path('powersupply/',views.powersupply_view),
    path('storage/',views.storage_view),
    path('videocard/',views.videocard_view),

   
    path('cpu/search/', views.search_view_cpu),
    path('motherboard/search/', views.search_view_motherboard),
    path('cpucooler/search/', views.search_view_cpucooler),
    path('case/search/', views.search_view_case),
    path('memory/search/', views.search_view_memory),
    path('powersupply/search/', views.search_view_powersupply),
    path('storage/search/', views.search_view_storage),
    path('videocard/search/', views.search_view_videocard),
  

    path('cart/', views.cart_view,name='cart'),
    path('cart-mb/', views.cart_view_motherboard,name='cart-mb'),


    path('add-to-cart/<int:pk>/', views.add_to_cart_view,name='add-to-cart'),
    path('add-to-cart-mb/<int:pk>/', views.add_to_cart_view_motherboard,name='add-to-cart-mb'),


    path('remove-from-cart/<int:pk>/', views.remove_from_cart_view,name='remove-from-cart'),
    path('remove-from-cart-mb/<int:pk>/', views.remove_from_cart_view_mb,name='remove-from-cart-mb'),
    
    
]