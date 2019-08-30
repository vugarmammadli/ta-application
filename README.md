# TA Application API

A simple part of a TA application system using the RESTful API approach using [Python Django Web Framework](https://www.djangoproject.com/) and [Django REST Framework](https://django-rest-framework.org) which is a powerful and flexible toolkit for building Web APIs.

The final version of the project can be found [here](https://ta-application-django.herokuapp.com/applicants/).

## REST Specifications
### Applicants
- `GET /applicants/`  Get all applicants. The JSON will return the following information about each applicants: Student number,  Given name,  Family name, Status, Year, and Courses which is a list of courses that applicant is applied for.
- `GET /applicants?status=status`  Filter all applicants with a given status (eg. Undergrad, MSc, PhD, MScAC, MEng). The JSON will return the same information as above.
- `GET /applicants?fname=fname`  Filter all applicants with a given Family Name. The JSON will return the same information as above.
- `POST /applicants/`  Add a new applicant. Required fields are *student_number*, *given_name*, *family_name*, *status*, *year*.
- `GET /applicant/student_number/` Get the information about an individual applicant with a particular student number.
- `DELETE /applicant/student_number/` Remove an applicant and all the applications related to this applicant.

### Courses
- `GET /courses/` Get all available courses. The JSON will return the following information about each courses: code, name, and description.
- `GET /courses?course=code` Filter a course with a particular code.
- `POST /courses/` Add a new course. Required fields are *code*, *name* and *description*.

### Applications
- `GET /applications` Get all applications which applicants are applied for courses with a ranking and an experience level. The JSON will return the following information about each applications: applicant (the student number of applicant), course (the code of the course), rank, and experience.
- `POST /applications/` Applicant applies TAship for a course. Required fields are *applicant*, *course*, *rank* and *experience*.

## How to run

- First of all, please make sure that you have installed [Python](https://www.python.org/downloads/) in your machine.
- Install virtualenv globally as well
```pip install virtualenv```
- Clone this repository to your local machine
```git clone https://github.com/vugarmammadli/ta-application.git```
- Change your directory to this repository
```cd ta-application```
- Create your virtual environment
```virtualenv venv -p python3```
```source venv/bin/activate```
- Install all the requirements for this project
```pip install -r requirements.txt```
- Make all migrations
```python manage.py makemigrations```
```python manage.py migrate```
- Run it
```python manage.py runserver```
- Finally, enjoy :)
```http://127.0.0.1:8000/applicants/```

## Extra details

Please refer to [examples.txt](./examples.txt) file for example requests and responses.

Here is the list of sources I used while developing this project:

 - https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-1
 - https://github.com/lucrae/django-cheat-sheet#ticket-creating-a-model
 - https://naveenlabs.com/2018/12/25/custom-serializer-related-field-using-django-rest-framework/
  - https://stackoverflow.com/questions/51574946/how-to-get-some-fields-in-inner-join-from-django
