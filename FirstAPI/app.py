#this program is the first program for creating a API
from flask import Flask, jsonify, request

# Intitialise the app
app = Flask(__name__)

# Define what the app does
@app.get("/")
def index():
    name  = request.args.get("name")
    response = {"data":f"Hello, {name}"}
    return response