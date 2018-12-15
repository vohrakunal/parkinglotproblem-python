# parkinglotproblem-python
Famous Parking Lot problem Using Python and Django
ver 2.2  *Designed by kv*

## Requirements
    Python 3.4+
    A supported version of Django (currently 1.11+)

## Files Description

#### Current Status of slots (Occupied/Vacant)
> http://www.your_hostname/api/

#### Add or Delete a Parking Slot and view currently parked cars
> http://www.your_hostname/api/parking/

#### Superuser login
> http://www.your_hostname/api/login/

#### Search
> http://www.your_hostname/api/search/
> > Can only be accessed if logged in
> > Search using car registration number and car color and get output in the form of parking slot, parking level, registration number and color

#### Logout
> http://www.your_hostname/api/logout/
> > Clear all login values


## Deployment

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



## Build With
* [Python3](https://www.python.org/downloads/) - Python3 
* [Django](https://docs.djangoproject.com/en/1.11/) - The web framework used
* [MySQL](https://dev.mysql.com/downloads/connector/python/) - Backend Database

## Authors
* **Kunal Vohra** -*Owner and Developer*- [kv](https://github.com/kunalvohra94)
> For any suggestions or improvements write to me. 

