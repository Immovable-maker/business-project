Django의 폼 기능은 복잡한 유효성 검사 규칙을 처리하며 모델 및 뷰와 완전히 분리되어 있습니다

Django에서 폼을 생성하는 것은 모델을 정의하는 것과 유사합니다

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

form = ContactForm(request.POST)
if form.is_valid():
    name = form.cleaned_data['name']
    email = form.cleaned_data['email']
    message = form.cleaned_data['message']

form의 errors 속성으로는 폼 오류에 액세스도 가능

ModelForm 클래스는 몇 줄의 코드로 모델을 기반으로 복잡한 폼을 생성할 수 있는 강력한 도구입니다.

폼들의 자세한 부분은 chapter3/myproject 참고하기

myapp/ 에 forms.py를 새로 만들었음 myapp/templates/ 이것도 당연히 같이 만듦 

myapp/ 에 urls.py를 새로 만들었음 프로젝트 측은 자동으로 만들어지는데 얘는 아닌가봐 

project urls를 app 쪽 urls와 migration 시키네 

결정적으로 책이 틀림

settings.py 에 templates DIR을 설정해준다음, myapp/create_book.html로 보내면 됨, 그니까 최상위부터 접근할 필요가 없는거지 

