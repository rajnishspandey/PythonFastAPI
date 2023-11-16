#this program is the first program for creating a API
from flask import Flask, jsonify, request

# Intitialise the app
app = Flask(__name__)

# Define what the app does
@app.get("/")
def index():
    fname  = request.args.get("fname")
    lname  = request.args.get("lname")
    fullname = request.args.get("fullname")
    #handeling the errors
    if not (fname or lname or fullname):
        error_message = "pleae try other keyword it's and error"
        error = {"status":error_message}
        return jsonify(error)
    response = {"data":f"Hello, {fname or  lname or fullname}"}
    return response