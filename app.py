from collegeapp.models import *
from sqlalchemy import text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(app.config.get('SQLALCHEMY_DATABASE_URI'))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db.create_all()
db.session.commit()

with open('trigger.sql', 'r') as f:
    sql = text(f.read())
result = db.engine.execute(sql)

if __name__ == '__main__':
    app.run(debug=True)


