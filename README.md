RSSLookup
=========

`RSSLookup` is a small lightweight, fast, python app for searching and booking RSS feed. It's default BBC feed. User can search RSS item and add to favorite per session.

Installation
------------

+ Install following dependancies via pip  before clonning app

```python
 pip install flask
 pip install xmltodict
 pip install flask-triangle
 pip install Flask-SQLAlchemy
```

 API Call
 --------

|API Call|Descriptoin|
|--------|-----------|
|http://0.0.0.0:5000|Default API Root|
|http://0.0.0.0:5000/api/rss/|RSS API default BBC feed as output|
|http://0.0.0.0:5000/api/rss/<rss_url>|Parameterised RSS call with URL|

Deployment
----------

Deploy app at Herokuapp. App can be push to live enviroment via following command

```git
git push heroku master
```



API call via following call
|URL |Type|Description|
|--------|---|-----------|
|**https://limitless-falls-83579.herokuapp.com/display** |WEB APP | API call with feed url argument|
|https://limitless-falls-83579.herokuapp.com/api/rss|WEB API | Default BBC News feed |
|https://limitless-falls-83579.herokuapp.com/api/rss/<URL> |WEB API | API call with feed url argument|




TODO
----

* ~~Create web api for feed~~
* Write test for API
* ~~Template for front end user~~
* ~~Search feed items (ng)~~
* ~~favorite functionality (ng) ~~(partially)
