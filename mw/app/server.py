__author__ = 'ehan'

from flask import Flask, render_template, request, redirect, url_for
from time import gmtime, strftime
import json

app = Flask(__name__)

@app.route('/summary')
def summaryPage():
    print("called summary")
    return render_template("tutorial/summary.html")

@app.route('/')
def homePage():
    return render_template("tutorial/index.html")

if __name__ == '__main__':
  app.run(debug=True)
