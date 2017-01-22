RSSLookup
=========

`RSSLookup` is a small lightweight app, fast, python app based on flask framework. It's default list the BBC feed. User can search RSS item and add to favorite per session

Installation
------------

+ Clone this repository via running

```git
git clone https://github.com/webbyfox/rss_lookup.git
```

+ Install pip if it's not install already. get-pip.py is provided via this repository. Just run


```python
 python get-pip.py
 pip install flask
 pip install xmltodict
 pip install flask-triangle
 pip install s
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
|URL |Type|Descriptoin|
|--------|---|-----------|
|**https://limitless-falls-83579.herokuapp.com/display** |APPLICATION | API call with feed url argument|
|https://limitless-falls-83579.herokuapp.com/api/rss|API | Default BBC News feed |
|https://limitless-falls-83579.herokuapp.com/api/rss/<URL> |API | API call with feed url argument|




TODO
----

* ~~Create web api for feed~~
* Write test for API
* ~~Template for front end user~~
* ~~Search feed items (ng)~~
* ~~favorite functionality (ng) ~~(partially)
