from flask import Flask, render_template, request
from random import randrange

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html', name="Donald")


@app.route('/result', methods=['get', 'post'] )
def result():

    firstname = request.form['firstname']
    lastname = request.form['lastname']
    print("Firstname = " + firstname)
    return "Thank you! " + firstname
