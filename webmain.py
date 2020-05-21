# Uros Krcadinac 2020
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
sh = LangUtilSh(fp)


# BASE ROUTES
# homepages in english and serbian

@app.route("/")
def false_home():
    return render_template('test/falsebase.html', params=en.params())


@app.route("/work/")
def home():
    return render_template('home.html', params=en.params())


@app.route("/rad/")
def home_s():
    return render_template('home.html', params=sh.params())


# PROJECT LIST SECTION
# rendering project_list.html

@app.route("/work/projects/")
def projects():
    project_list, data = utils.projects(fp, en)
    return render_template('project_list.html', projects=project_list, params=en.params(), data=data)


@app.route("/rad/projekti/")
def projects_s():
    project_list, data = utils.projects(fp, sh)
    return render_template('project_list.html', projects=project_list, params=sh.params(), data=data)


# PROJECTS FILTERED
# rendering filtered list of projects, also project_list.html

@app.route("/work/projects/<by>/<criteria>")
def projects_by_category(by, criteria):
    list, data = utils.projects_by_category(fp, en, by, criteria)
    return render_template('project_list.html', projects=list, params=en.params(), data=data)


@app.route("/rad/projekti/<by>/<criteria>")
def projects_by_category_s(by, criteria):
    list, data = utils.projects_by_category(fp, sh, by, criteria)
    return render_template('project_list.html', projects=list, params=sh.params(), data=data)


# PROJECT SECTION
# rendering project.html

@app.route('/work/projects/<name>/')
def project(name):
    this_project = fp.get_or_404('{}/{}'.format(en.dir(), name))
    return render_template('project.html', project=this_project, params=en.params())


@app.route('/rad/projekti/<name>/')
def project_s(name):
    this_project = fp.get_or_404('{}/{}'.format(sh.dir(), name))
    return render_template('project.html', project=this_project, params=sh.params())


# WRITING SECTION
# texts and books

@app.route('/work/writing/')
def writing():
    page, data = utils.writing(fp, en)
    return render_template('writing.html', params=en.params(), page=page, data=data)


@app.route('/rad/tekstovi/')
def writing_s():
    page, data = utils.writing(fp, sh)
    return render_template('writing.html', params=sh.params(), page=page, data=data)


# TEACHING SECTION
# sillabi and workshops

@app.route('/work/teaching/')
def teaching():
    page, data = utils.teaching(fp, en)
    return render_template('writing.html', params=en.params(), page=page, data=data)


@app.route('/rad/edukacija/')
def teaching_s():
    page, data = utils.teaching(fp, sh)
    return render_template('page.html', params=sh.params(), page=page, data=data)


# SPEAKING SECTION
# talks and public lectures

@app.route('/work/speaking/')
def speaking():
    page, data = utils.speaking(fp, en)
    return render_template('page.html', params=en.params(), page=page, data=data)


@app.route('/rad/nastupi/')
def speaking_s():
    page, data = utils.speaking(fp, sh)
    return render_template('page.html', params=sh.params(), page=page, data=data)


# PRESS SECTION
# press and media

@app.route('/work/press/')
def press():
    page, data = utils.press(fp, en)
    return render_template('page.html', params=en.params(), page=page, data=data)


@app.route('/rad/mediji/')
def press_s():
    page, data = utils.press(fp, sh)
    return render_template('page.html', params=sh.params(), page=page, data=data)


# ABOUT SECTION
# biography

@app.route('/work/about/')
def about():
    page, data = utils.about(fp, en)
    return render_template('about.html', params=en.params(), page=page, data=data)


@app.route('/rad/bio/')
def about_s():
    page, data = utils.about(fp, sh)
    return render_template('about.html', params=sh.params(), page=page, data=data)


# TESTING SECTION
# alternative design

@app.route('/work/projects1/<name>/')
def project1(name):
    path = '{}/{}'.format(en.dir(), name)
    this_project = fp.get_or_404(path)
    return render_template('project1.html', project=this_project, params=en.params())


# ADDITIONAL ROUTES
# synesketch, download, etc.

@app.route('/synesketch/')
def synesketch():
    return redirect("/work/projects/synesketch", code=302)


@app.route('/download/<path:args>')
def download_file(args=None):
    items = args.split("/")
    path = '{}/{}'.format("static", "download")
    for i in items:
        path = path + "/" + i
    print(path)
    # return send_file(path, as_attachment=True)
    return send_file(path)


@app.route('/3/')
def poem():
    return render_template('test/3.html')


# MAIN
# starting app

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        # app.run(host='0.0.0.0', debug=True)
        app.run(host='127.0.0.1', debug=True)
        # app.run(host='0.0.0.0')
