# Django Booking Platform
#### Originally forked from [manjurulhoque/django-job-portal](https://github.com/manjurulhoque/django-job-portal)

## Description
 An open source online booking platform based on django and sqlite3.
 
 User is divided into visitor and owner. Owner can add new object to the listing and modify the details. Visitor can search and see the listing to get more information.

 To be implemented: booking function

Tech Stack:

1. Django
2. Sqlite

## Setup
### Installation

1. Create a virtual environment

    `python3 -m venv venv`

2. Activate it

    `source venv/bin/activate`

3. Clone the repository and install the packages in the virtual env:

    `pip install -r requirements.txt`


### Run

1. (Only applicable when debug=True) With the venv activated, execute:

    `python manage.py collectstatic`

2. Create initial database:

    `python manage.py migrate`

3. Load demo data (optional): TODO

4. Run server:

    `python manage.py runserver`

### Run test:
TODO

### To dump data:
TODO
