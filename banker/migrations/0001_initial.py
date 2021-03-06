# Generated by Django 4.0.2 on 2022-02-08 20:20

import banker.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=64, verbose_name='Nazwa konta')),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=14, verbose_name='Stan konta')),
                ('account_number', models.CharField(default=banker.models.generate_account_number, max_length=30, verbose_name='Numer konta')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Właściciel konta')),
            ],
        ),
    ]
