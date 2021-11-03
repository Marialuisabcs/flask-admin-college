from flask import Flask
import os
from pathlib import Path

database_name = "admin"
db_uri = "postgresql+psycopg2://" + os.path.join(Path.cwd(), (database_name + ".db"))
db_uri_format = r'{}'.format(db_uri)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri_format
app.config['SECRET_KEY'] = '567041680499569'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from collegeapp import views

