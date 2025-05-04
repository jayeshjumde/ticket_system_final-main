from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ShowListView, BookTicketView, BookingHistoryView, AdminShowListView, AdminShowCreateView, AdminShowUpdateView, AdminShowDeleteView, AdminBookingListView, AdminDashboardView
from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('shows/', views.ShowListView.as_view(), name='show_list'),
    path('book/<int:show_id>/', views.BookTicketView.as_view(), name='book_ticket'),
    path('booking-history/', views.BookingHistoryView.as_view(), name='booking_history'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    # admin paths
    path('admin-dashboard/', views.AdminDashboardView.as_view(), name='admin_dashboard'),
    path('admin/shows/', views.AdminShowListView.as_view(), name='admin_show_list'),
    path('admin/shows/create/', views.AdminShowCreateView.as_view(), name='admin_show_create'),
    path('admin/shows/update/<int:pk>/', views.AdminShowUpdateView.as_view(), name='admin_show_update'),
    path('admin/shows/delete/<int:pk>/', views.AdminShowDeleteView.as_view(), name='admin_show_delete'),
    path('admin/bookings/', views.AdminBookingListView.as_view(), name='admin_booking_list'),
]