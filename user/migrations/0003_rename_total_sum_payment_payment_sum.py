# Generated by Django 5.0.6 on 2024-06-27 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='total_sum',
            new_name='payment_sum',
        ),
    ]
