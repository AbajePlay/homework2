# Generated by Django 5.1.4 on 2024-12-19 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_remove_ticket_city_remove_ticket_date_ticket_concert'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
