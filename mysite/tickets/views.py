from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket, Concert, Review, PromoCode
from django.core.mail import send_mail
from django.http import JsonResponse

def home(request):
    concerts = Concert.objects.order_by('date')
    reviews = Review.objects.order_by('-created_at')[:10]
    return render(request, 'home.html', {'concerts': concerts, 'reviews': reviews})

def buy_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    date = ticket.concert.date
    city = ticket.concert.city

    if request.method == 'POST':
        name = request.POST['first-name']
        surname = request.POST['last-name']
        email = request.POST['email']

        promo_code = request.POST.get('promo_code', '').strip()

        if promo_code:
            try:
                promo = PromoCode.objects.get(code=promo_code)
                if promo.is_valid():
                    discount = promo.discount
                else:
                    promo.delete()
            except PromoCode.DoesNotExist:
                discount = 0

        send_mail(
            'Ваш билет на концерт',
            f'Здравствуйте, {name} {surname}, ваш билет на концерт в городе {city}, {date} успешно оформлен!',
            'noreply@concert.com',
            [email],
            fail_silently=False,
        )
        return redirect('success')

    return render(request, 'buy_ticket.html', {'ticket': ticket, 'date': date, 'city': city})

def success(request):
    return render(request, 'success.html')

def reviews(request):
    reviews = Review.objects.order_by('-created_at')[:10]
    return render(request, 'home.html', {'reviews': reviews})

def leave_review(request):
    if request.method == 'POST':
        name = request.POST['name']
        text = request.POST['text']
        Review.objects.create(name=name, text=text)
        return redirect('review_confirm')
    return render(request, 'review.html')

def review_confirm(request):
    return render(request, 'reviewconfirm.html')

def validate_promo_code(request):
    code = request.GET.get('code', '').strip()
    try:
        promo = PromoCode.objects.get(code=code)
        if promo.is_valid():
            return JsonResponse({'valid': True, 'discount': promo.discount})
    except PromoCode.DoesNotExist:
        pass
    return JsonResponse({'valid': False})