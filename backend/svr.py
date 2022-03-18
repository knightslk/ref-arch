from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/random")
def random_cwe():
    ran_cwe = str(random.randrange(1,1500))
    return "https://cwe.mitre.org/data/definitions/"+ran_cwe+".html"
