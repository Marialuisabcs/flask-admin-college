from flask import Flask

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://ygjqxvmmslyfod:0cefce656bf0f55ec4c070c19a9a249c556bd3866d64d1be0cf2d67b069229a0@ec2-34-203-114-67.compute-1.amazonaws.com:5432/d1sgr0fu0rbh6r"
app.config['SECRET_KEY'] = '567041680499569'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['BABEL_DEFAULT_LOCALE'] = "PT"

from collegeapp import views
