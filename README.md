RSSLookup
=========

`RSSLookup` is a small lightweight app, fast, open source flask RSS lookup app. It's default list the BBC feed.

Installation
------------

..code-block:: python
 
 python get-pip.py

 pip install flask
 
 pip install xmltodict


 API Call
 --------

|API Call|Descriptoin|
|--------|-----------:|
|http://0.0.0.0:5000|Default API Root|
|http://0.0.0.0:5000/api/rss/|RSS API default BBC feed as output|
|http://0.0.0.0:5000/api/rss/<rss_url>|Parameterised RSS call with URL|

