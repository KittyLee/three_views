# -*- coding: utf-8 -*-

from app import app
from flask import render_template

@app.route('/')
def index():
	return render_template("Home.html")


@app.route('/secondview')
def feedback():
	return render_template("secondview.html")

@app.route('/thirdview')
def issues():
	return render_template("thirdview.html")


@app.route('/forthview')
def worker():
	return render_template("forthview.html")
