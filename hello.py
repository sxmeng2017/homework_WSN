import matplotlib
matplotlib.use('Agg')
from flask import Flask
from flask import render_template, flash, redirect,url_for, session, jsonify
from flask import request
from config import Config
from form import LoginForm, DataForm
from Leach import result
from time import sleep


app = Flask(__name__)
app.config.from_object(Config)

#@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():

    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'john'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/user/<name>')
def user(name):
    return '<h1>hello!,{}!</h1>'.format(name)


#@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/')
@app.route('/leach_data', methods=['GET'])
def leach_data():
    form = DataForm()
    return render_template('leach_data.html', form=form)

@app.route('/leach_data', methods=['POST'])
def leach_data_():
    form = DataForm()
    if form.validate_on_submit():
        r = form.data.data
        data = result(r)
        post = {
            'r': r,
            'data': data
        }
        session['leach_data'] = post
        return redirect(url_for('leach'))

@app.route('/combine', methods=['GET'])
def combine():
    form = DataForm()
    return render_template('combine.html', form=form)


@app.route('/combine', methods=['POST'])
def combine_post():
    if request.method == 'POST':
        r = int(request.form.to_dict()['data'])
        data, dst = result(r)
        return jsonify(data=data, dst=dst)


@app.route('/leach', methods=['GET', 'POST'])
def leach():
    return render_template('leach.html', post=session['leach_data'])


if __name__ == '__main__':
    app.run(debug=True)

