## 운영체제에 파이썬 설치
### Linux
sudo apt update
sudo apt install python3

## Django 프로젝트를 위한 가상 환경 만들기
pip3 install virtualenv

디렉토리 이동

python3 -m virtualenv myenv

source myenv/bin/activate

활성화된 상태에서 

pip install django (django-admin --version으로 확인하기)


## Django 프로젝트 생성 
source 로 가상 환경 활성화 하기

django-admin startproject example_project

cd example_project

python manage.py runserver 

로 개발 서버 실행으로 확인

