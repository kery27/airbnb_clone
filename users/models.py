from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import reverse
from core import managers as core_managers


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

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGING_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
        (LOGING_KAKAO, "Kakao"),
    )

    avatar = models.ImageField(upload_to="avatas", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRUNCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)

    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )

    # objects = core_managers.CustomModelManager()
    objects = core_managers.CustomUserManager()

    # 유저 모델이 변경되면 이걸 호출함
    # 업데이트 뷰를 써서 유저정보를 업데이트 했을때 변경이 일어난걸알고 이걸 불러
    # url에 profile을 pk 값을 가지고 호출해.
    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})
