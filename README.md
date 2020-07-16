python 라이브러리 설치 명령어
pip install virtualenv
virtualenv 명령어를 이용해서 가상환경을 만드는 방법
virtualenv [원하고자하는 프로젝트명]
virtualenv lecture_3 && cd lecture_3
1

가상환경 활성화
가상환경 할성화 명령어 activate.bat

Scripts 폴더내에 존재

cd Scripts && activate
가상환경 비활성화
가상환경 비할성화 명령어 deactivate.bat

Scripts 폴더내에 존재

cd Scripts && deactivate
설치한 라이브러리 관리는 requirements.txt에서 관리된다.
freeze 명령어를 이용해서 생성
생성방법

pip freeze > requirements.txt
requirements.txt 를 활용해서 라브러리 설치
pip install -r requirements.txt


//////////////////////////////////////////////
python library 설치 명령어



pip or pip 3 install < 원하고자하는 라이브러리 명 >

pip install virtualenv

virtualenv 명령어를 이용해서 가상환경을 만드는 방법 : 

virtualenv [원하고자 하는 프로젝트 명]

  virtualenv lecture_3 && cd lecture_3  - 여기까지 가상환경 만들 준비한것

가상환경 활성화를 하기 위한 명령어 activate.bat(script안에 존재)

따라서 cd Scripts  && activate(.bat생략가능) - 이때부터 가상공간이 구축됨



가상환경 비활성화방법 deactivate.(bat생략가능) -Scripts폴더



deactivate



설치한 모든 프로젝트를 관리하는 방법

requirements.txt에서관리

freeze 명령어를 이용해서 생성

생성방법(프로젝트가 시작된 곳에서 만들어주면 된다.)

​     pip freeze > requirements.txt



requirements.txt를 활용해서 라이브러리 설치

pip install -r requirements.txt

