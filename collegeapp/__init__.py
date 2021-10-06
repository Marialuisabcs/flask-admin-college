from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/Documentos/1-Faculdade/2021.2/LBD/Trabalho/admin.db'
app.config['SECRET_KEY'] = '567041680499569'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from collegeapp import views

