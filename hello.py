import matplotlib
matplotlib.use('Agg')
import os
from flask import Flask
from flask import render_template, flash, redirect,url_for, session, jsonify
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask import request
from config import Config
from form import LoginForm, DataForm, UploadForm
from Leach import result
import cv2
from amiya import perd


app = Flask(__name__)
app.config.from_object(Config)
basedir = os.path.abspath(os.path.dirname(__file__))
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

#@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return '<h1>hello!,{}!</h1>'.format(name)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


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

@app.route('/predict_load', methods=['GET', 'POST'])
def predict_load():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = photos.url(filename)
        res = perd(basedir + "/static/image/" + filename)[0][0]
    else:
        file_url, res= None, None
    return render_template('predict_load.html', form=form, file_url=file_url, res=res)


if __name__ == '__main__':
    app.run(debug=True)

