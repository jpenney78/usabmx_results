from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    url = {'url': 'URL'}
    return render_template('index.html', title='Results Form', url=url)
    