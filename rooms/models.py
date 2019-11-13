from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

# Create your models here.
# 추상 클래스를 만들어준건 룸타입을 추가 하기 위해서
# 룸타입 말고도 아이템을 쓸게 여러개 있기때문이라고 한다?
# 추상 클래스로 하고 구현하는 클래스(상속받은) 클래스가 데이터베이스를 생성하게끔한다

# 룸의 성격이 있고 성격을 종류별로 나열할때 필요한게 아이템
# 사람이란 모델이 있고 코라는 성격이 있다. 코는 성격인데 어떤 코인지 나열할 수 있게 해주는게 아이템
# 입이 성격인데 입에도 종류가 있으므로 이걸 아이템으로 나눌수 있기 때문에 아이템이란 추상클래스를 만든것
# 입이란 성격에도 아이템을 먹이고 코라는 성격에도 아이템을 먹인거다
# 이렇게 못하는 사람의 성격은 뭘까 그럼.. 보유한 현금금액?? 이런 성격은 궂이 아이템으로 나눌수 없을듯

# 룸타입 - 몇인실인가.. 말고 하우스룰 - 금연,동물금지,노파티 같은 애들.. 콤보라고 생각하면되려나
# 이런 애들을 추상 클래스로 만들고 얘는 이름이 필요하다로 만든거
class AbstractItem(core_models.TimeStampedModel):
    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


# 추상 클래스를 상속받은 룸타입을 만들어준다
# 궂이 추상 아이템을 만든이유는 더 나중을 위한거라고 보자
# 내가 룸타입만 아이템이 필요했으면 추상 아이템을 만들지 않았겟지만
# 만들었다... 강의에서 더 필요할거라니 만들었어.. 따라가보자....
# 아직 많이 헷갈린다.. 매니투매니는 알겠는데
# 룸모델 안에서 다시 클래스를 만들고 그 클래스를 참조하는 경우라니..
# 유저를 참조하는 호스트는 포린키 룸타입을 참조하는 룸타입은 룸모델안에 다른 클래스.
# 이대로만 하면 실제 화면에서(어드민에서) 추가기능을 넣을수 없어서 어드민을 고쳐주자
class RoomType(AbstractItem):
    """RoomType Object Options """

    class Meta:
        verbose_name = "RoomType"


class Amenity(AbstractItem):
    """ Amenity Object Options"""

    class Meta:
        verbose_name = "Amenitie"


class Facility(AbstractItem):
    """ Facility Model Definition"""

    class Meta:
        verbose_name = "Facilitie"


class HouseRule(AbstractItem):
    """ Rule model Definition """

    class Meta:
        verbose_name = "House Rule"


# 사진은 룸아래 룸은 사용자 아래 위치한다.
# 룸 클래스 위에 룸을 포린키로 물리면 룸을 인식 못하므로 스트링으로 바꿔줘야한다
class Photo(core_models.TimeStampedModel):
    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


# class Room(models.Model):
class Room(core_models.TimeStampedModel):

    """Room Model Definition """

    name = models.TextField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guest = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        user_models.User, related_name="rooms", on_delete=models.CASCADE
    )
    # room_type = models.ManyToManyField(RoomType, blank=True)
    room_type = models.ForeignKey(
        RoomType, related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField(Amenity, related_name="rooms", blank=True)
    facilities = models.ManyToManyField(Facility, related_name="rooms", blank=True)
    house_rules = models.ManyToManyField(HouseRule, related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    # 전체에서 쓰일 리뷰의 전체 평균을 구하는 함수
    # 룸과리뷰는 포린키로 물려있지 룸 -> 리뷰 관계이므로 room안에는 review_set이 있고 리뷰셋은 reviews로 바꿧지
    # 따라서 룸을 리뷰한 라뷰에 접근이 가능하다.
    # 방에 대한 리뷰들의 평균을 구하는게 레이팅 에버리지고 이건 리뷰모델안에 있다
    # 방에 리뷰가 여러개가 달릴수 있으므로 전체의 평균을 구할때는 총 리뷰들의 합을 리뷰한갯수로 나눠야함
    # 쿼리셋으로 가져온 올리뷰. 길이를 구하는 len으로 리뷰갯수를 구함

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating_average()
        return all_ratings / len(all_reviews)

    # 저장할때 저장 말고 다른이벤트를 오버라이드 하는거야
    # 저장할때 특정 행동을 하도록 여기에 다시쓰는거야.
    # 모든곳에서 이 이벤트는 모델에 접근 할거기 때문에 발생가능하다
    # 그래서 너가 어드민에서만 발생하길 원한다면 어드민 에서도 이기능을 쓸수 있다. 약간다름
    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)
