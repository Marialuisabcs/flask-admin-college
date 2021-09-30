from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import event

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/Documentos/1-Faculdade/2021.2/LBD/Trabalho/admin.db'
app.config['SECRET_KEY'] = '567041680499569'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class DashboardView(AdminIndexView):

    def is_visible(self):
        # This view won't appear in the menu structure
        return False

    """
    @expose("/")
    def index(self):
        return self.render('admin/home.html')
    
    admin = Admin(app, "MadeInStockholm.se", index_view=HomeView(name='Home'))
    """


admin = Admin(app,
              name='Trabalho de LBD',
              template_mode='bootstrap3',
              index_view=DashboardView()
              )


class Aluno(db.Model):
    __tablename__ = 'aluno'
    id_aluno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    rga = db.Column(db.String(12), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id_curso', ondelete='CASCADE'))
    curso = db.relationship("Curso")


class Curso(db.Model):
    __tablename__ = 'curso'
    id_curso = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False, unique=True)
    faculdade = db.Column(db.String(20), nullable=False)
    coordenador_id = db.Column(db.Integer, db.ForeignKey('professor.id_professor', ondelete='CASCADE'))
    coordenador = db.relationship("Professor")


class Professor(db.Model):
    __tablename__ = 'professor'
    id_professor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    cpf = db.Column(db.String(11), nullable=False, unique=True)


class Materia(db.Model):
    __tablename__ = 'materia'
    id_materia = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=True)
    carga_horaria = db.Column(db.Integer, nullable=False)


class MatriculadoEm(db.Model):
    __tablename__ = 'matriculadoEm'
    materia_id = db.Column(db.ForeignKey('materia.id_materia', ondelete='CASCADE'), primary_key=True)
    aluno_id = db.Column(db.ForeignKey('aluno.id_aluno', ondelete='CASCADE'), primary_key=True)
    aluno = db.relationship("Aluno")
    materia = db.relationship("Materia")


class LecionadaPor(db.Model):
    __tablename__ = 'lecionadaPor'
    materia_id = db.Column(db.ForeignKey('materia.id_materia', ondelete='CASCADE'), primary_key=True)
    professor_id = db.Column(db.ForeignKey('professor.id_professor', ondelete='CASCADE'), primary_key=True)
    professor = db.relationship("Professor")
    materia = db.relationship("Materia")


db.create_all()
db.session.commit()

admin.add_view(ModelView(Aluno, db.session))
admin.add_view(ModelView(Curso, db.session))
admin.add_view(ModelView(Professor, db.session))
admin.add_view(ModelView(Materia, db.session))
admin.add_view(ModelView(MatriculadoEm, db.session))
admin.add_view(ModelView(LecionadaPor, db.session))

with app.app_context():
    event.listen(db.engine, 'connect', lambda con, rec: con.execute('pragma foreign_keys=ON'))


@app.route('/')
@app.route('/home')
def home():
    """inserir os dados do trabalho e um botao que leva ao admin
    Returns:
        Text: Template renderizado
    """
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run()
