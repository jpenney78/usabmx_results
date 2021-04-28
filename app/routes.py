from flask import render_template, flash, request, redirect
from app import app
from app.forms import RequestForm
from app.results_to_csv import get_results


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/request', methods=['GET', 'POST'])
def request_results():
    if request.method == 'POST':
        req = request.form
        results = get_results(req.get('results_url'))
        return render_template('results.html', title='Results', results=results)
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
