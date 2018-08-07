[![Build Status](https://travis-ci.org/wagolemusa/My-Diary.svg?branch=Challenge-2)](https://travis-ci.org/wagolemusa/My-Diary)
[![Coverage Status](https://coveralls.io/repos/github/wagolemusa/My-Diary/badge.svg?branch=Challenge-3)](https://coveralls.io/github/wagolemusa/My-Diary?branch=Challenge-3)
[![Maintainability](https://api.codeclimate.com/v1/badges/e29fcbc2317c1e18ebe5/maintainability)](https://codeclimate.com/github/wagolemusa/My-Diary/maintainability)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)
![Jenkins tests](https://img.shields.io/jenkins/t/https/jenkins.qa.ubuntu.com/view/Precise/view/All%20Precise/job/precise-desktop-amd64_default.svg)

# My-Diary
MyDiary is an online journal where users can pen down their thoughts and feelings. 

### Set up the environment
This platform APIs is bult on the top of flask python framwork.

Clone the repository
```sh
git@github.com:wagolemusa/My-Diary.git
```
Create the virtual environment and install dependencies
```sh
cd My-Diary
```

```sh
virtualenv env
```
Activate the virtual environment
```sh
source /venv/bin/activate
```
Install dependencies

```sh
pip install install -r requirements.txt
```
### Run the applicattion

```sh
python app.py
```
### APIs Endpoints

**`POST /api/v2/auth/signup`** *Register*

**`POST /api/v2/auth/login`**    *Login*

**`GET  /api/v2/entries`**  *All Users*

**`POST /api/v2/entries`** *Post Entry*

**`GET  /api/V2/entries/<entry:id>`** *Get only one entry*

**`GET /api/v2/entries`** *Get all Entries*

**`PUT /api/v2/entries/<entry:id>/`** *Update an Entry*

**`DELETE /api/v2/entries/<entry:id>`** *Delete an Entry*
