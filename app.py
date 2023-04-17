from flask import Flask
from sqlalchemy import create_engine
import os
from bll.views import views

app = Flask(__name__)
db = create_engine(os.environ['DB_SIGNEDIN_URI'])


app.add_url_rule('/', view_func=views.start)
app.add_url_rule('/login/', view_func=views.login)
app.add_url_rule('/registration/', view_func=views.registration, methods=['GET', 'POST'])


if __name__ == "__main__":
    app.run(debug=True)
