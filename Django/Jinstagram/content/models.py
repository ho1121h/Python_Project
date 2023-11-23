from django.db import models

# Create your models here.
# 모델 생성 후 터미널에 python manage.py makemigrations content 를 입력 (잠깐만~ 우선 settings에 content 폴더를 app에 등록했는지 생각해보라)
class Feed(models.Model):
    content = models.TextField() # 내용
    image = models.TextField() # 피드 이미지
    profile_image = models.TextField() # 프로필 이미지
    user_id = models.TextField() # 글쓴이
    like_count = models.IntegerField() # 좋아요 수
