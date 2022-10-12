from flask import Flask, request

app = Flask(__name__)

@app.get('/welcome')
def welcome_message():
    '''prints welcome message on screen'''
    html = "<body><h1> welcome </body></h1>"
    return html

@app.get('/welcome/home')
def welcome_home_message():
    '''prints welcome home message on screen'''

    html = "<body><h1> welcome home </body></h1>"
    return html

@app.get('/welcome/back')
def welcome_back_message():
    '''prints welcome back message on screen'''
    html = "<body><h1> welcome back </body></h1>"
    return html
