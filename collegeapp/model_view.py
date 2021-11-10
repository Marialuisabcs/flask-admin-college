from flask import flash
from flask_admin.contrib.sqla import ModelView
from sqlalchemy.exc import IntegrityError


class MyModelView(ModelView):

    def delete_model(self, model):
        try:
            self.on_model_delete(model)
            self.session.flush()
            self.session.delete(model)
            self.session.commit()

        except IntegrityError:
            flash(f'IntegrityError: Você não pode deletar esse(a) {self.name}', 'error')
            self.session.rollback()

            return False

        except Exception as ex:
            if not self.handle_view_exception(ex):
                flash(f'Failed to delete record. {ex}', 'error')

            self.session.rollback()

            return False
        else:
            self.after_model_delete(model)

        return True


class CantCrud(ModelView):
    can_edit = False
    can_create = False
