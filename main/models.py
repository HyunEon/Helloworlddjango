from django.db import models

# Create your models here.
# 관계형 데이터베이스로 생각했을 때 테이블을 여기에 선언하는 듯
# __str__ 메소드는 파이썬에 객체 출력했을 때 반환할 내용을 정의함
# __str__ 반환할 때 반드시 String으로 반환해야 함, 다른 형이면 오퍼레이션 타입 에러 뜸.
class MotivationQuotes(models.Model):
    name = models.CharField(max_length=100)
    quotes = models.TextField()

    def __str__(self):
        return self.name
