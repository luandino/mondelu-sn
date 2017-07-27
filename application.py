#!/usr/bin/env python
import flask

import os
from flask import Flask, jsonify, request, url_for, render_template, redirect, send_from_directory, session as login_session


from flask_bootstrap import Bootstrap

def create_app():
  app = Flask(__name__)
  Bootstrap(app)
  return app

app = Flask(__name__)
app.config['DEBUG'] = True

def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)
app.jinja_env.globals['url_for_other_page'] = url_for_other_page

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')




@app.route('/')
def index():
    #if 'username' in login_session:
    #    return 'You are logged in as ' + login_session['username']
    return flask.render_template('index.html')





if __name__ == '__main__':
    app.secret_key = 'fdsfmkrtjkfmdslfjfssgshfklsnvdsklj'
    app.run()
