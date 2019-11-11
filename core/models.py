from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    # 누가 자동으로 이 모델을 생성할 경우에 크리에이트에 시간을 생성해준다
    # 누가 자동으로 업데이트 할경우에 시간을 저장해준다

    #
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    # 이 모델을 쓰는 다른 모델들... 어차피 얘는 상속용 공통 클래스 이므로
    # 걔내들이 모델을 생성한다. 데이터를 생성할거기 때문에
    # 여기다가 선언해줄게 있다는것. 추상적인 모데이라는걸로.
    # 앱스트랙 유저를 상속했을때 그안에 모든걸 다 생성하지 않았듯?????
    class Meta:
        abstract = True
