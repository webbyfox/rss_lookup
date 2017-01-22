from flask import Flask
from flask import render_template
from flask import abort
from flask import jsonify
from flask import request

import urllib2
from urllib2 import URLError
import xmltodict
from flask_triangle import Triangle
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
Triangle(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


@app.route('/')
def index():
    return jsonify({"/": "Welcome to RSS 2 JSON WEB API",
                    "/api/rss/": "Default API gateway with BBC feed",
                    "/api/rss/<url>": "URL to fetch API gateway"})


@app.route('/display')
def display():
    return render_template('display.html')

def rss_to_dict(rss_url):
    rss_data = None
    try:
        rss_data = urllib2.urlopen(rss_url)
    except (URLError, ValueError) as e:
        abort(404)
    if rss_data:
        data = rss_data.read()
        rss_data.close()
        data = xmltodict.parse(data)
        return data


@app.route('/api/rss/')
@app.route('/api/rss/<path:rss_url>')
def get_tasks(rss_url='https://feeds.bbci.co.uk/news/rss.xml?edition=uk'):
    return jsonify({'Response': rss_to_dict(rss_url)})


@app.route('/api/fav/add/', methods=['GET'])
def not_allowed():
    response = jsonify({
        "ErrorMessage": "GET method is not allowed"
    })
    return response


@app.route('/api/fav/add/', methods=['POST'])
def add_url():
    if 'url' not in request.form:
         abort(400)
    item = Favourites(request.remote_addr, request.form['url'])
    db.session.add(item)
    db.session.commit()
    return 'Created'


@app.route('/api/fav/', methods=['GET'])
def get_all_fav():
    fav_list = Favourites.query.filter_by(ip_address=request.remote_addr).all()
    return jsonify({'response':  str([item.url for item in fav_list])})

@app.errorhandler(404)
def page_not_found(e):
    response = jsonify({
      "ErrorMessage" : "Please provide valid RSS link"
       })
    return response


class Favourites(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    ip_address = db.Column(db.String(255))
    url = db.Column(db.String(255))
    add_on = db.Column(db.Date)
    created_by = db.Column(db.String(50))

    def __init__(self, ip_address, url):
        self.ip_address = ip_address
        self.url = url
        self.add_on = datetime.now().date()
        self.created_by = 'apiuser'




if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
