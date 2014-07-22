__author__ = 'ehan'

from flask import Flask, render_template, request, redirect, url_for
from time import gmtime, strftime
import json

app = Flask(__name__)

@app.route('/summary', methods=['GET','POST'])
def summaryPage():
    app.logger.info("called summary api")
    message = None
    if request.method == "POST":
        message = {
            'firstname': request.form['firstname'],
            'lastname': request.form['lastname'],
            'year': request.form['year'],
            'department': request.form['department'],
            'course1': request.form['course1'],
            'course2': request.form['course2'],
            'course3': request.form['course3'],
        }
        app.logger.info(message)
        return render_template("tutorial/summary.html", message=message)
    else:
        return render_template("tutorial/summary.html", message=message)

@app.route('/')
def homePage():
    return render_template("tutorial/index.html")

if __name__ == '__main__':
  app.run(debug=True)
