# Drawingdiary

## Requirements

- Python 3.4.2
- Django 1.9.6
- Pillow 3.2.0

## Dev config

- editorconfig

## Local setting

python

``` shell
$ git clone git@github.com:hyejeongpark/drawingdiary.git
$ cd drawingdiary
$ pyvenv env
$ . env/bin/activate
(env) $ pip install -r requirements.txt
(env) $ python manage.py migrate
(env) $ python manage.py createsuperuser
(env) $ python manage.py runserver
```
