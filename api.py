from flask import Flask
from flask import render_template
from flask import abort
from flask import  jsonify

import urllib2
from urllib2 import URLError
import xmltodict

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"/": "Welcome to RSS 2 JSON WEB API",
                    "/api/rss/": "Default API gateway with BBC feed",
                    "/api/rss/<url>": "URL to fetch API gateway"})


def rss_to_dict(rss_url):
    rss_data = None
    try:
        rss_data = urllib2.urlopen(rss_url)
    except URLError,ValueError:
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


@app.errorhandler(404)
def page_not_found(e):
    response = jsonify({
      "ErrorMessage": "Please provide valid RSS link"
    })
    return response
    #return render_template('404.html', content=content), 404


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)