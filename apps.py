import sqlalchemy
from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os
import views


app = Flask(__name__)
db = create_engine(os.environ['DB_SIGNEDIN_URI'])
base = declarative_base()


app.add_url_rule('/', view_func=views.start)
app.add_url_rule('/login/', view_func=views.login, methods=['POST', 'GET'])


if __name__ == "__main__":
    app.run(debug=True)
