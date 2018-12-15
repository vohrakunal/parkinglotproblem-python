# parkinglotproblem-python
Famous Parking Lot problem Using Python and Django
ver 2.2  *Designed by kv*

## Requirements
    Python 3.4+
    A supported version of Django (currently 1.11+)

## Steps To Install

### Install django *ver 1.11 LTS*
```
$ pip install django==1.11
```
Install MySQL and do the modifications below
Create a database aps
Import aps.sql using
```
$ mysql -u <mysql_username> -p aps < aps.sql
```

> change MySQL USER:'mysql_username', PASS:'mysql_password', HOST and PORT address in aps/settings [default values: (USER': 'django', 'PASSWORD':'django', 'HOST': 'localhost','PORT': '')]

### Run Migrations
> change directory to home_folder/aps
> python manage.py makemigrations
> python manage.py migrate

### Create a USER
```
$ python manage.py createsuperuser
Username (leave blank to use 'default_user'):
Email address:
Password:
Password (again):

Superuser created successfully.
```

### Run Server
```
$ python manage.py runserver
```
Open URL
> hostname:8000/


Description
1. http://www.your_hostname/api/
    -> Current Status of slots (Occupied/Vacant)

2. http://www.your_hostname/api/parking/
    -> Add or Delete a Parking Slot
    -> View Currently parked cars

3. http://www.your_hostname/api/login/
    -> User Superuser username and password to login

4. http://www.your_hostname/api/search/
    -> Can only be accessed if logged in
    -> Search using car registration number and car color and get output in the form of parking slot, parking level, registration number and color

5. http://www.your_hostname/api/logout/
    -> Clear all login values


# # KNOWN ISSUES
1. 
