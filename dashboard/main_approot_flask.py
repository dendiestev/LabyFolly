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
    return render_template("index.html", texte="<b>un mot<b/>", liste=l_lead, dico= {"cle1": 12, "cle2": (1, 2)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)