# Generated by Django 5.1.4 on 2024-12-15 14:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_concert'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='city',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='date',
        ),
        migrations.AddField(
            model_name='ticket',
            name='concert',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='tickets.concert'),
            preserve_default=False,
        ),
    ]
