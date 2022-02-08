from django.db import models
from django.contrib.auth.models import User
import random


def generate_account_number():
    def rndm_part():
        return random.randint(1000, 9999)
    account_number = f'10000 {rndm_part()} {rndm_part()} {rndm_part()} 0000 {rndm_part()}'
    return account_number


class UserAccount(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Właściciel konta'
    )
    account_name = models.CharField(
        max_length=64,
        verbose_name='Nazwa konta'
    )
    balance = models.DecimalField(
        default=0.00,
        max_digits=14,
        decimal_places=2,
        verbose_name='Stan konta'
    )
    account_number = models.CharField(
        default=generate_account_number,
        max_length=30,
        verbose_name='Numer konta'
    )
