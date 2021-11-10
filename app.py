from collegeapp.models import *
from sqlalchemy import text

db.drop_all()
db.create_all()
db.session.commit()

with open('trigger.sql', 'r') as f:
    sql = text(f.read())
result = db.engine.execute(sql)

if __name__ == '__main__':
    app.run(debug=True)
