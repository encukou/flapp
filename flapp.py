import datetime

from flask import Flask, url_for, render_template
from jinja2 import Markup
app = Flask(__name__)

@app.route('/')
def index():
    kus_html = Markup('<b>aho<i>j</i></b>')
    now = datetime.datetime.now()
    return render_template(
        'hello.html',
        now=now,
        kus_html=kus_html)

@app.route('/hello/<name>/')
def hello(name):
    return render_template('hello.html',
                           name=name,
                           count=3)

@app.template_filter('time')
def human_time(t):
    return t.strftime("%Y")

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, port=12843)
