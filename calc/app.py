# Put your app in here.

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/add")
def add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"{a + b}"


@app.route("/sub")
def sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"{a - b}"


@app.route("/mult")
def mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"{a * b}"


@app.route("/div")
def div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"{a / b}"


operations = {"add": add, "sub": sub, "mult": mult, "div": div}


# requires a and b as parameters for above functions to work
# @app.route("/math/<operation>")
# def math(operation):
#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     return f"{operations[operation](a, b)}"
