RSSLookup
=========

`RSSLookup` is a small lightweight app, fast, open source flask RSS lookup app. It's default list the BBC feed.

Installation
------------

1. Install pip via downloading [get-pip.py](https://bootstrap.pypa.io/get-pip.py) and then run

```python
  python get-pip.py
```
2. Install flask via pip command

```python
 pip install flask
```

3. Install xmltodict module to convert xml data to dictionaries

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

