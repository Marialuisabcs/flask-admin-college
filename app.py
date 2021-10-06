from collegeapp.models import *

db.create_all()
db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)
