from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# 앱스트랙 유저를 상속받아서 사용해봣다. 여러가지가 이미 만들어져있고 그위에 내것만 얹는다는거지
class User(AbstractUser):
    """ User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"
    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRUNCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))
    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean"))

    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRUNCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
