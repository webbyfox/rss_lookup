RSSLookup
=========

`RSSLookup` is a small lightweight app, fast, python app based on flask framework. It's default list the BBC feed. User can search RSS item and add to favorite per session

Dependancies
------------

+ Install pip via downloading [get-pip.py](https://bootstrap.pypa.io/get-pip.py) and move file to your project folder and run


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

 API Call
 --------

|API Call|Descriptoin|
|--------|-----------|
|http://0.0.0.0:5000|Default API Root|
|http://0.0.0.0:5000/api/rss/|RSS API default BBC feed as output|
|http://0.0.0.0:5000/api/rss/<rss_url>|Parameterised RSS call with URL|



TODO
----

* ~~Create web api for feed~~
* Write test for API
* Template for front end user
* Search feed items (ng) 
* favorite functionality (ng)
 