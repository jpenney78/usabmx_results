from flask import render_template
from app import app
from app.forms import RequestForm


@app.route('/')
@app.route('/index')
def index():
    url = {'url': 'URL'}
    return render_template('index.html', title='Results Form', url=url)


@app.route('/request', methods=['GET', 'POST'])
def request():
    form = RequestForm()
    if form.validate_on_submit():
        flash('Url={}, States={}'.format(
            form.results_url.data, form.state_list.data))
        return redirect('/index')
    return render_template('request.html', title='Get Results', form=form)
