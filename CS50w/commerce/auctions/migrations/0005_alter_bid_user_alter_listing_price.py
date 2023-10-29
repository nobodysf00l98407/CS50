# Generated by Django 4.2.5 on 2023-10-19 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0004_bid_alter_listing_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bid",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="userBid",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="price",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="currentBid",
                to="auctions.bid",
            ),
        ),
    ]