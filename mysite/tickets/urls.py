from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('buy/<int:ticket_id>/', views.buy_ticket, name='buy_ticket'),
    path('success/', views.success, name='success'),
    path('review/', views.leave_review, name='leave_review'),
    path('review/confirm/', views.review_confirm, name='review_confirm'),
    path('validate-promo-code/', views.validate_promo_code, name='validate_promo_code'),
]
