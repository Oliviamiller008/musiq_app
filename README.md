# musiq_app

## Installation
Install lastest version of Python at https://www.python.org/downloads/ 

Create a directory for the project in your File Explorer. 

In command prompt, navigate to the directory you just created (using cd command).

Create python virtual environment by typing:
```bash
py -m venv env 
```

Start virtual environment:
```bash
env\Scripts\activate
```

Install django:
```bash
pip install django
```

## Running The Web Page 
Navigate into the directory for the project on the command line.

Run the server:
```bash
py manage.py runserver
```

Copy and paste the address that is returned into a web browser.

## Running the MySql database on local server
Note: MySQL database will be updated/changed using python only - no real need to access MySQL database tables unless curious.

Run the server:
```bash
py manage.py runserver
```

Install Xampp: https://www.apachefriends.org/download.html 

Run Xampp Control Panel:
- Start Apache & MySQL
- Click on Admin of MySQL Service

Run these two commands server:
```bash 
py manage.py migrate
py manage.py runserver
```
Reference for any help: https://data-flair.training/blogs/django-database/


















