from flask_restful import Api
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import PersonClient
from Persons import Persons

app = Flask("app")
api = Api(app)
Bootstrap(app)

persons = {}

@app.route("/")
def main():
    return render_template('index.html', name='hej', persons=persons)

@app.route("/fetch")
def fetch():
    print('fetch')
    persons = get_persons()
    print(persons)
    return render_template('index.html', name='hej', persons=persons)


def get_persons():
    return Persons(PersonClient.getPersons()).get()


app.run(port=8000, debug=True)
