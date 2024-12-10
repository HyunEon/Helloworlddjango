from django.contrib import admin
from .models import MotivationQuotes

# Register your models here.
# 어드민.py에 모델을 등록시키면 편하게 관리자 페이지에서 데이터를 관리할 수 있다.

# python manage.py makemigrations
# python manage.py migrate
# 테이블 업데이트 후 오류가 난다면 마이그레이션 돌리자

# 중간에 테이블 스키마 타입이나 이름을 변경했을 때 오퍼레이션 오류가 나오는 경우가 있는데
# python manage.py migrate --run-syncdb
# 싱크 디비 넣어서 다시 돌리면 해결됨.

admin.site.register(MotivationQuotes)
