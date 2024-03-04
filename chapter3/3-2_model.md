Django에서 모델은 django.db.models.Model 클래스를 상속하는 Python 클래스입니다. 모델의 각 속성은 데이터베이스 필드를 나타냅니다.


DRY 법칙 dont repeat yourself

중복을 제거 - 일관성, 오류가능성 하락, 수정을 쉽게 

추상화와 재사용 - 검증 리스크 감소, 재사용 편함, 단순화 일관성유지

단일 진리 원칙 - 단일 진리원칙을 따르면 정보를 단일 위치에서 관리함

---
Django 모델 데이터 유형
Django 모델을 사용할 때는 여러 가지 필드 유형을 사용하여 데이터베이스 테이블의 구조와 데이터 유형을 정의할 수 있습니다. Django에서 일반적으로 사용되는 일부 모델 필드는 다음과 같습니다:

CharField: 이 필드는 문자열을 나타내며 텍스트 데이터를 저장하는 데 사용됩니다. max_length 매개변수를 사용하여 문자열의 최대 길이를 지정할 수 있습니다.
IntegerField: 이 필드는 정수 값을 나타냅니다. 양수와 음수 정수 모두를 특정 범위 내에서 저장할 수 있습니다.
FloatField: 이 필드는 소수점 숫자를 나타냅니다. 지정된 소수 자릿수를 가진 부동 소수점 숫자를 저장할 수 있습니다.
BooleanField: 이 필드는 불리언 값(True 또는 False)을 나타냅니다. 이진 값이나 플래그를 저장하는 데 사용할 수 있습니다.
DateField: 이 필드는 날짜 값을 나타냅니다. "YYYY-MM-DD" 형식으로 날짜를 저장할 수 있습니다.
DateTimeField: 이 필드는 날짜와 시간 값을 나타냅니다. "YYYY-MM-DD HH:MM:SS" 형식으로 날짜와 시간 정보를 모두 저장할 수 있습니다.
EmailField: 이 필드는 이메일 주소를 나타냅니다. 입력된 값이 유효한 이메일 주소인지를 검증합니다.
FileField: 이 필드는 파일 업로드를 나타냅니다. 파일 경로나 실제 파일 객체를 저장할 수 있습니다.
ForeignKey: 이 필드는 두 모델 간의 다대일 관계를 정의하는 데 사용됩니다. 다른 모델을 외래 키로 참조하는 데 사용됩니다. 이 필드는 관련 모델을 지정해야 하며, 일대다와 같은 관계를 설정하는 데 사용할 수 있습니다.
ManyToManyField: 이 필드는 두 모델 간의 다대다 관계를 정의하는 데 사용됩니다. 하나의 모델 인스턴스를 다른 모델 인스턴스와 여러 개 관련시킬 수 있습니다. 이 필드는 관련 모델을 지정해야 하며, 관계를 관리하기 위해 중간 테이블을 생성합니다.

OneToOneField 각 어플마다 고유한 사용자 프로필
> class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

ForeignKey 하나의 포스트에 여러 코멘트가 붙을 수 있음 
> class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.TextField()

ManyToManyField 블로그 글에 여러개 태그, 태그에 여러 블로그 글 가능
> class Tag(models.Model):
    name = models.CharField(max_length=30)
    posts = models.ManyToManyField(BlogPost)

[https://wikidocs.net/197548] 클래스 다이어그램은 여기서 관계도 보세요 제발

---
```
python manage.py makemigrations
```
어플리케이션 migrations/ 디렉토리에 있으며 DB 스키마를 어떻게 변경할지에 대한 정보를 담고 있음

```
python manage.py migrate
```
위에서 적힌 수정 내용에 따라 데이터베이스에 대응하는 스키마 변경 작업을 수행합니다. 
이 작업은 새로운 테이블 생성, 필드 추가 또는 수정, 인덱스 생성 등과 같은 데이터베이스 스키마의 변화를 반영합니다

---

ORM을 이용하여 직접 SQL을 사용하는 대신 파이썬 메소드로 작성합시다.
```
# 모델의 모든 인스턴스 검색
instances = YourModel.objects.all()

# 필터링된 인스턴스 검색
filtered_instances = YourModel.objects.filter(your_field='your_value')

# 단일 인스턴스 검색
instance = YourModel.objects.get(id='your_id')

# 여러 개의 필터 조건 연결
filtered_instances = YourModel.objects.filter(your_field1='value1', your_field2='value2')

# 대소문자 구분 없는 포함 여부 확인
filtered_instances = YourModel.objects.filter(your_field__icontains='value')

# 관계를 걸쳐 조회
filtered_instances = Entry.objects.filter(blog__name='Django')

# 새 인스턴스 생성
new_instance = YourModel.objects.create(your_field='your_value')

# 인스턴스 업데이트
instance.your_field = 'new_value'
instance.save()

```

필터링:

filter(**kwargs): 주어진 조회 매개변수와 일치하는 QuerySet을 반환합니다.
exclude(**kwargs): 주어진 조회 매개변수와 일치하지 않는 QuerySet을 반환합니다.
get(**kwargs): 주어진 조회 매개변수와 일치하는 단일 객체를 반환합니다. 일치하는 항목이 없을 경우 DoesNotExist 예외를 발생시키며, 여러 개의 일치하는 항목이 있을 경우 MultipleObjectsReturned 예외를 발생시킵니다.
first(): QuerySet에서 첫 번째 객체를 반환합니다.
last(): QuerySet에서 마지막 객체를 반환합니다.
쿼리 연결:

filter().exclude(): 여러 개의 필터링 조건을 연결할 수 있습니다.
filter().order_by(): 결과의 정렬 순서를 지정할 수 있습니다.
filter().values(): 모델 인스턴스 대신 딕셔너리를 포함하는 QuerySet을 반환합니다.
집계:

aggregate(**kwargs): QuerySet에서 집계 작업(개수 세기, 합산, 평균 등)을 수행합니다.
어노테이션:

annotate(**kwargs): 제공된 어노테이션을 기반으로 QuerySet의 각 객체에 추가 필드를 추가합니다.
관련 객체:

select_related(): 조인을 사용하여 관련된 객체를 단일 데이터베이스 쿼리로 가져옵니다.
prefetch_related(): 관련된 객체를 효율적으로 가져오기 위해 별도의 쿼리에서 미리 가져옵니다.
조인과 관계:

join(): 테이블 간에 명시적인 조인을 수행합니다.
select_related(): 조인을 사용하여 관련된 객체를 가져와 데이터베이스 쿼리 수를 줄입니다.
prefetch_related(): 별도의 쿼리를 사용하여 관련된 객체를 효율적으로 가져옵니다.
reverse(): 역방향 관계를 따라 관련된 객체를 가져옵니다.
정렬과 정렬 순서:

order_by(*fields): 지정된 필드를 기준으로 QuerySet을 정렬합니다.
reverse(): QuerySet의 순서를 반전시킵니다.
제한과 슬라이싱:

all(): QuerySet에 있는 모든 객체를 반환합니다.
values_list(*fields): 모델 인스턴스 대신 튜플을 포함하는 QuerySet을 반환합니다.
values(*fields): 모델 인스턴스 대신 딕셔너리를 포함하는 QuerySet을 반환합니다.
distinct(): 고유한 값을 가진 QuerySet을 반환합니다.