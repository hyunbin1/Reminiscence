<h1> 기본 세팅 설명서 </h2>

# Reminiscence

📖 Introduction()

1. project = reminiscence

2. app = main, accounts

3. 아직 기본적인 세팅만 해놓았습니다!

- main App에는 index, detail, create html 총 3개의 페이지를 생성해놓았고,
  기본적으로 불러올수 있도록 url연결과 views.py 페이지 불러오기 함수만 작성해 놓았습니다.
- accounts App에는 login, signup.html 총 2개의 페이지를 생성해놓았고,
  view나 url은 작성하지 않았습니다.

4. 브랜치는 마스터, back으로 나누었습니다.

🏁 Getting started

1. git clone
   First of all, clone this repository

\$ git clone https://github.com/hyunbin1/ToyProject.git

2. venv 파일 지우고 다시 깔기
   python -m venv venv . venv/scripts/activate

3. 가상환경 활성화하기
   $ source venv/scripts/activate # for windows
$ source venv/bin/activate # for mac or linux

4. pip package 깔기

\$ pip install -r requirements.txt

cf] If you want people to recommend the package you have installed, enter the command.

\$ pip freeze > requirements.txt
If additional packages are installed, the following commands should be executed.

5. 브랜치 변경하기

- master, back

\$ git checkout 브랜치명

:Common times when you start project : Git command
when you start the project=
$ git pull origin <branch_name>
Plz don't forget to push your work, when the work is done.
$ git add .
$ git commit -m "What did u do"
$ git push origin <branch_name>
