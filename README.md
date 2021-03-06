# REST API with Flask, Flask-RESTful and SQLite.

## Description:
Simple RESTFul Flask application (still in development) with bunch of automated API tests. Main reason for developing this app is writing automated tests against exposed endpoints (with usage of Python requests library, Postman (form manual testing) and REST Assured (Java) in the near future).

So far active endpoints are:

GET /users

GET /users/name

DELETE /users/name

POST /register

GET /products

GET /product/name

POST /product/name

GET /history/name

POST /shopping

POST /auth


App deployed on Heroku if you don't want to run it locally:

https://flask-rest-api-demo.herokuapp.com

If after clicking on the Heroku link, __Application Error__ is displayed, all free Dyno hour were used.

### Steps to run app and tests:

1.Install Python (tested on Python 3.5.2, Linux Ubuntu 16.04 LTS)

2.Create virtualenv

3.Download project from GitHub

4.Go to root folder of the project, install required modules:

```
$ make deps
```

5.To run app:

```
$ python app.py
```

Then in Postman (have to be installed on your system), you can import collection of URL's from __postman__ folder placed in root folder of the downloaded app.

6.To run automated API tests, open terminal/console and run app, then open another terminal/console window, go to __tests__ folder and enter command:

```
$ python user_endpoint_test.py
```
