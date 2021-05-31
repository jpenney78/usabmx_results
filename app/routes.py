from flask import render_template, flash, request, redirect
from app import app
from app.forms import RequestForm
from app.results_to_csv import get_results
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/request', methods=['GET', 'POST'])
def request_results():
    if request.method == 'POST':
        logging.info('posted')
        req = request.form
        try:
            results = get_results(req.get('results_url'))
            logging.info(f"results: {results}")
            return render_template('results.html', title='Results', results=results)
        except:
            logging.exception('exception')
            pass
    else:
        form = RequestForm()
        if form.validate_on_submit():
            flash('Url={}, States={}'.format(
                form.results_url.data, form.state_list.data))
            return redirect('/index')
        return render_template('request.html', title='Get Results', form=form)

#def index():
#    url = {'url': 'URL'}
#    return render_template('index.html', title='Results Form', url=url)
