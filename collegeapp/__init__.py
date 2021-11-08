from flask import Flask

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = "postgres://ckkiyfgygbrzhw:4322377416b4cd6eef6fca8d241fad52e8b856ac8bedfb3f177a9a050859882c@ec2-54-147-207-184.compute-1.amazonaws.com:5432/da8gi3mhaqotkc"
app.config['SECRET_KEY'] = '567041680499569'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['BABEL_DEFAULT_LOCALE'] = "PT"

from collegeapp import views
