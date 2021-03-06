from django.db import models
from django.urls import reverse

"""""""""""
★ 필드옵션 : 필드마다 고유 옵션이 존재, 공통 적용 옵션도 있음
null (DB 옵션) : DB 필드에 NULL 허용 여부 (디폴트 : False)
unique (DB 옵션) : 유일성 여부 (디폴트 : False)
blank : 입력값 유효성 (validation) 검사 시에 empty 값 허용 여부 (디폴트 : False)
default : 디폴트 값 지정. 값이 지정되지 않았을 때 사용
verbose_name : 필드 레이블. 지정되지 않으면 필드명이 쓰여짐
validators : 입력값 유효성 검사를 수행할 함수를 다수 지정
각 필드마다 고유한 validators 들이 이미 등록되어있기도 함
예 : 이메일만 받기, 최대길이 제한, 최소길이 제한, 최대값 제한, 최소값 제한 등
choices (form widget 용) : select box 소스로 사용
help_text (form widget 용) : 필드 입력 도움말
auto_now_add : Bool, True 인 경우, 레코드 생성시 현재 시간으로 자동 저장
"""""""""""

"""""""""""
★ 필드타입
CharField : 문자열. max_length 설정이 가능하다
TextField
ImageField : 이미지
DateField : 날짜/시간
BooleanField, NullBooleanField : 참/거짓
IntegerField : 숫자
BinaryField, FileField : 파일
EmailField : 이메일
URLField : 링크
"""""""""""

# Create your models here.

class Request(models.Model):
    subject = models.CharField(max_length=50, blank=True)   #제목
    name = models.CharField(max_length=50, blank=True)  #담당자
    created_date = models.DateField(null=True, blank=True)  #신청일
    finished_date = models.DateField(null=True, blank=True) #마감일
    mail = models.CharField(max_length=50, blank=True)  #이메일
    memo = models.CharField(max_length=200, blank=True) #메모
    hits = models.IntegerField(null=True, blank=True)   #조회수`

    def __str__(self):
        return "제목 : " + self.subject + ", 담당자 : " + self.name + ", 작성일 : " + str(self.created_date) + ", 마감일 : " + str(self.finished_date) + ", 메일 : " + self.mail + ", 메모 : " + self.memo + ", 조회수 : " + str(self.hits)

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])   #현재 글번호(id)값에 해당하는 detail 페이지로 이동




