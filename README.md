[![Build Status](https://travis-ci.org/wagolemusa/My-Diary.svg?branch=Challenge-2)](https://travis-ci.org/wagolemusa/My-Diary)

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

**`POST /api/v1/auth/register`** *Register*

**`POST /api/v1/auth/login`**    *Login*

**`GET  /api/v1/get_all_users`**  *All Users*

**`POST /api/v1/post_entry`** *Post Entry*

**`GET  /api/V1/view_entry/<int:id>`** *Get only one entry*

**`GET /api/v1/get_entries`** *Get all Entries*

**`PUT /api/v1/update_entry/<id>/`** *Update an Entry*

**`DELETE /api/v1/delete_entry/<int:id>`** *Delete an Entry*

```sh
Heroku app
```
https://mydiaryandela.herokuapp.com/