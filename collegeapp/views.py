from flask_admin import Admin

from collegeapp.model_view import MyModelView, CantCrud
from collegeapp.models import *

admin = Admin(app,
              name='Trabalho de LBD',
              template_mode='bootstrap3',
              url='/'
              )

admin.add_view(MyModelView(Professor, db.session))
admin.add_view(MyModelView(Curso, db.session))
admin.add_view(MyModelView(Aluno, db.session))
admin.add_view(MyModelView(Materia, db.session))
admin.add_view(MyModelView(MatriculadoEm, db.session))
admin.add_view(MyModelView(LecionadaPor, db.session))
admin.add_view(CantCrud(Log, db.session))
