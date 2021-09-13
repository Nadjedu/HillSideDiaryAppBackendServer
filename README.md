# HillSideDiaryAppBackendServer
Backend Service Layer for HillSide App

### Requirements
1. Python > 3.7 
2. Pip
3. mysql server or mysql-client Check [here](https://pypi.org/project/mysqlclient/)

### Installation/Setup Steps 

1. run ` $ git clone https://github.com/Nadjedu/HillSideDiaryAppBackendServer.git`
2. run ` $ cd HillSideDiaryAppBackendServer`
3. Create a virtual environment and activate it.
4. run ` $ python setup.py` to install the dependencies and create a .env file.
5. run ` $ gcloud auth login` (Authenticates and acquires credentials for the Cloud SQL API)
6. run ` $ gcloud config set project hillside-project`
7. Download and install the Cloud SQL Auth proxy for your OS (Step 2) from [here](https://cloud.google.com/python/django/appengine#connect_sql_locally)

You're done :tada:

### How to run the server locally
1. In a separate terminal start the SQL proxy by running `$ ./cloud_sql_proxy -instances=hillside-project:us-east1:hillside=tcp:5432`
2. In a different terminal run ` $ python manage.py runserver`

### Documentation Guides
1. [Django](https://www.djangoproject.com/)
2. [Django Rest Framework](https://www.django-rest-framework.org/)
3. [Google Cloud with Django](https://cloud.google.com/python/django/appengine)

### Contribution guidelines ###
* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Nana Adjedu, Hugo Olcese, Ackerley Colin, Cooley Nick, Hull Allen, Xia Sally
 
