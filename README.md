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
 ```
+ Install flask via pip command

```python
 pip install flask
```

+ Install xmltodict module to convert xml data to dictionaries

```python
 pip install xmltodict
```

+Install flask-triangle for an

```python
pip install flask-triangle
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

Deploy app via Heroku build for CI. App can be push to live enviroment via following command

```git
git push heroku master
```

Main RSS app at:
https://limitless-falls-83579.herokuapp.com/display 

API call via following call

https://limitless-falls-83579.herokuapp.com/api/rss - default BBC News feed 
https://limitless-falls-83579.herokuapp.com/api/rss/<URL>


TODO
----

* ~~Create web api for feed~~
* Write test for API
* ~~Template for front end user~~
* ~~Search feed items (ng)~~
* favorite functionality (ng)
 