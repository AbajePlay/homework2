from django.contrib import admin
from .models import Concert, Review, PromoCode

@admin.register(Concert)
class ConcertAdmin(admin.ModelAdmin):
    list_display = ('city', 'date')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'text')
    search_fields = ('name', 'text')
    list_filter = ('created_at',)

@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'expiration_date', 'created_at')
    search_fields = ('code',)
    list_filter = ('expiration_date', 'created_at')