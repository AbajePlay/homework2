from django.db import models
from django.utils.timezone import now

class Concert(models.Model):
    city = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.city} - {self.date.strftime('%d/%m/%Y')}"

class Ticket(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE, related_name='tickets')
    user_name = models.CharField(max_length=100)
    user_surname = models.CharField(max_length=100)
    user_email = models.EmailField()

    def __str__(self):
        return f"{self.concert.city} - {self.concert.date}"

class Review(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%d/%m/%Y')}"

class PromoCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    expiration_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return self.expiration_date is None or self.expiration_date >= now().date()

    def __str__(self):
        return f"{self.code} ({'Бессрочный' if not self.expiration_date else self.expiration_date})"

