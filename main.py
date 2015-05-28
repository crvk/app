from flask_restful import Api
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import PersonClient
from Persons import Persons

app = Flask("app")
api = Api(app)
Bootstrap(app)

@app.route("/")
def main():
    persons = Persons(PersonClient.getPersons()).get()
    return render_template('index.html', name=persons[0]['first_name'], persons=persons)

app.run(debug=True, port=8000)
