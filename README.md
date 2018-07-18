[![Build Status](https://travis-ci.org/wagolemusa/My-Diary.svg?branch=master)](https://travis-ci.org/wagolemusa/My-Diary)
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