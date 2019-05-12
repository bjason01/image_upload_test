# ImageUpload with TestCase

This project is a really short guide to make a TestCase in order to receive a Image and send from the test.

#### The most important part of this project is in `uploadapp/tests.py`


## Steps to set up the project:

* Prepare venv

```
python3.7 -m venv .env
source .env/bin/activate
```

* Install dependencies

```
cd django-file-upload
pip install djangorestframework
```

* Run migrations

```
python manage.py migrate
```

* Run test

```
python manage.py test
```

The parent of this project is hosted in: https://www.techiediaries.com/django-rest-image-file-upload-tutorial/

