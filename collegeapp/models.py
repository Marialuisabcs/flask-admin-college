from collegeapp import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class Aluno(db.Model):
    __tablename__ = 'aluno'
    id_aluno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    rga = db.Column(db.String(12), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id_curso', ondelete='CASCADE'))
    curso = db.relationship("Curso")

    def __repr__(self):
        return self.nome


class Curso(db.Model):
    __tablename__ = 'curso'
    id_curso = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False, unique=True)
    faculdade = db.Column(db.String(20), nullable=False)
    coordenador_id = db.Column(db.Integer, db.ForeignKey('professor.id_professor', ondelete='CASCADE'))
    coordenador = db.relationship("Professor")

    def __repr__(self):
        return self.nome


class Professor(db.Model):
    __tablename__ = 'professor'
    id_professor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    cpf = db.Column(db.String(11), nullable=False, unique=True)

    def __repr__(self):
        return self.nome


class Materia(db.Model):
    __tablename__ = 'materia'
    id_materia = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=True)
    carga_horaria = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return self.nome


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

