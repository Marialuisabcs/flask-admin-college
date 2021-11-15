from collegeapp.models import *
from sqlalchemy import text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine(app.config.get('SQLALCHEMY_DATABASE_URI'))

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Session = scoped_session(sessionLocal)

session = Session()
db.create_all()
db.session.commit()
Session.remove()

session_trigger = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Session_trigger = scoped_session(session_trigger)

session_trigger = Session()

with open('trigger.sql', 'r') as f:
    sql = text(f.read())
result = db.engine.execute(sql)

Session_trigger.remove()

if __name__ == '__main__':
    app.run(debug=True)
