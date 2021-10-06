from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from collegeapp.models import *
from sqlalchemy import event



admin = Admin(app,
              name='Trabalho de LBD',
              template_mode='bootstrap3',
              url='/'
              )


admin.add_view(ModelView(Aluno, db.session))
admin.add_view(ModelView(Curso, db.session))
admin.add_view(ModelView(Professor, db.session))
admin.add_view(ModelView(Materia, db.session))
admin.add_view(ModelView(MatriculadoEm, db.session))
admin.add_view(ModelView(LecionadaPor, db.session))

with app.app_context():
    event.listen(db.engine, 'connect', lambda con, rec: con.execute('pragma foreign_keys=ON'))