from flask import Flask, render_template, request, session, redirect
from random import randrange
import api_client

app = Flask(__name__)

# Set the secret key is used to encrypt the session cookie!
app.secret_key = b'asdkj<kjhsajhdlkasjhd918723oaisdjaposidj'

@app.route('/login')
def form():
    return render_template('form.html')


@app.route('/', methods=['get', 'post'] )
def result():

    username = request.form['username']
    password = request.form['password']
    print("username = " + username)
    print("password =  " + password)
    token = api_client.get_access_token(username, password)
    session['token'] = token
    return render_template('home.html')



@app.route('/angebote', methods=['get', 'post'] )
def angebote():
    angebote = api_client.get_angebote('L12153', session['token']).json()
    print(angebote)
    return render_template('angebote.html', angebote=angebote)
