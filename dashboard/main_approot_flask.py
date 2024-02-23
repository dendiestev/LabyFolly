#!/bin/bash
from flask import Flask
from flask import render_template
import sys
sys.path.append('../')
from bdd.requests_bdd import *



a = Bdd("../bdd/BDD.db")
l_lead = a.get_all()



app = Flask(__name__)
@app.route('/')
def fonction_1():
    return render_template("index.html", liste=l_lead)

@app.route('/about')
def fonction_2():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)