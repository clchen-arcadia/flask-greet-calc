from flask import Flask, request

app = Flask(__name__)

@app.get('/add')
def add():
    """Returns the sum of a and b"""

    a = int(request.args['a'])
    b = int(request.args['b'])

    return f"<html><body><h1> The sum is {a + b}</h1></body></html>"


@app.get('/subtract')
def subtract():
    """Returns the difference between a and b"""

    a = int(request.args['a'])
    b = int(request.args['b'])

    return f"<html><body><h1> The difference is {a - b}</h1></body></html>"


@app.get('/multiply')
def multiply():
    """Returns the product between a and b"""

    a = int(request.args['a'])
    b = int(request.args['b'])

    return f"<html><body><h1> The product is {a * b}</h1></body></html>"


@app.get('/divide')
def divide():
    """Returns the quotient between a and b"""

    a = int(request.args['a'])
    b = int(request.args['b'])

    return f"<html><body><h1> The quotient is {a / b}</h1></body></html>"
