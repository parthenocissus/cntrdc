# Uros Krcadinac 2021
# Main App

import sys
from flask import Flask, render_template, send_file, redirect
from flask_flatpages import FlatPages
from flask_frozen import Freezer
import utils
from langutil import LangUtilEn, LangUtilSh

app = Flask(__name__)

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'

app = Flask(__name__)
fp = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)

en = LangUtilEn(fp)

# BASE ROUTES
# homepage in english

@app.route("/")
def home():
    return render_template('base.html', params=en.params())


@app.route("/work/")
def home2():
    return render_template('home.html', params=en.params())



# PROJECT LIST SECTION
# rendering project_list.html

@app.route("/work/projects/")
def projects():
    project_list, data = utils.projects(fp, en)
    return render_template('project_list.html', projects=project_list, params=en.params(), data=data)


# PROJECTS FILTERED
# rendering filtered list of projects, also project_list.html

@app.route("/work/projects/<by>/<criteria>")
def projects_by_category(by, criteria):
    list, data = utils.projects_by_category(fp, en, by, criteria)
    return render_template('project_list.html', projects=list, params=en.params(), data=data)


# PROJECT SECTION
# rendering project.html

@app.route('/work/projects/<name>/')
def project(name):
    this_project = utils.project(fp, en, name)
    return render_template('project.html', project=this_project, params=en.params())



# WRITING SECTION
# texts and books

@app.route('/work/writing/')
def writing():
    page, data = utils.writing(fp, en)
    return render_template('page.html', params=en.params(), page=page, data=data)


# TEACHING SECTION
# sillabi and workshops

@app.route('/work/teaching/')
def teaching():
    page, data = utils.teaching(fp, en)
    return render_template('page.html', params=en.params(), page=page, data=data)


# SPEAKING SECTION
# talks and public lectures

@app.route('/work/speaking/')
def speaking():
    page, data = utils.speaking(fp, en)
    return render_template('page.html', params=en.params(), page=page, data=data)


# PRESS SECTION
# press and media

@app.route('/work/press/')
def press():
    page, data = utils.press(fp, en)
    return render_template('page.html', params=en.params(), page=page, data=data)


# NOTE LIST SECTION
# rendering note_list.html

@app.route("/work/notebook/")
def note_list():
    data = utils.note_list(fp, en)
    return render_template('note_list.html', params=en.params(), data=data)



# ABOUT SECTION
# biography

@app.route('/work/about/')
def about():
    page, data = utils.about(fp, en)
    return render_template('about.html', params=en.params(), page=page, data=data)





@app.route('/download/<path:args>')
def download_file(args=None):
    items = args.split("/")
    path = '{}/{}'.format("static", "download")
    for i in items:
        path = path + "/" + i
    print(path)
    # return send_file(path, as_attachment=True)
    return send_file(path)



# MAIN
# starting app

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(host='127.0.0.1', debug=True)
