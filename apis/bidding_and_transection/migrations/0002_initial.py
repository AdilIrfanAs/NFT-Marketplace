# Generated by Django 4.0 on 2021-12-30 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nft_management', '0001_initial'),
        ('accounts', '__first__'),
        ('bidding_and_transection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nfttransaction',
            name='nft',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nft_transaction', to='nft_management.nft'),
        ),
        migrations.AddField(
            model_name='nfttransaction',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nft_seller', to='accounts.user'),
        ),
    ]