from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    categoryName = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.categoryName}"


class Bid(models.Model):
    bid = models.IntegerField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="userBid"
    )


class Listing(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=512)
    imageURL = models.CharField(max_length=1024)
    price = models.ForeignKey(
        Bid, on_delete=models.CASCADE, null=True, blank=True, related_name="bidPrice"
    )
    isActive = models.BooleanField(default=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="user"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="category",
    )
    watchlist = models.ManyToManyField(
        User, blank=True, null=True, related_name="listingWatchlist"
    )

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):  # comment model
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="userComment",
    )  # author of the comment
    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="listingComment",
    )  # listing of the comment
    message = models.CharField(max_length=200)  # message of the comment

    def __str__(self):  # string representation of the model
        return f"{self.author} comment on {self.listing}"  # return the author and the listing
