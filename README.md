<h1> 기본 세팅 설명서 </h2>

# Reminiscence

Toy_project = 
===

📖 Introduction
---
<p>
  <h3>
1. project = reminiscence

2. app = main, accounts

3. 아직 기본적인 세팅만 해놓았습니다!

- main App에는 index, detail, create 총 3개의 html 페이지를 생성해놓았고,
  기본적으로 불러올수 있도록 url연결과 views.py 페이지 불러오기 함수만 작성해 놓았습니다.
  <br>
  <br>
- accounts App에는 login, signup 총 2개의 html 페이지를 생성해놓았고,
  view나 url은 작성하지 않았습니다.
<br>
4. 브랜치는 master, back으로 나누었습니다.
  </h3>
 </p>
 
<br>
 
🏁 Getting started
---

### 1. git clone

First of all, clone this repository

```bash
$ git clone https://github.com/hyunbin1/Reminiscence.git
```

### 2.  venv 파일 지우고 다시 깔기

```[terminal] bash
$ python -m venv venv
```
> The name of virtual environment is defined by "venv"

### 3. 가상환경 실행하기
```bash
$ source venv/scripts/activate # for windows
$ source venv/bin/activate # for mac or linux
```

### 4. pip packages 깔기

```bash
$ pip install -r requirements.txt
```

cf] If you want people to recommend the package you have installed, enter the command.

```bash
$ pip freeze > requirements.txt
```

> If additional packages are installed, the following commands should be executed.

### 5. git branch 변경하기


```bash
$ git checkout <branch_name> # "master" or "develop"
```

> Insert 'master' or 'back' instead of <branch_name>.


:Common times when you start project : Git command
---

```bash
when you start the project=
$ git pull origin <branch_name>
Plz don't forget to push your work, when the work is done.
$ git add .
$ git commit -m "What did u do"
$ git push origin <branch_name>
```

