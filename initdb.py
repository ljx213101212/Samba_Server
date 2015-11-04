__author__ = 'jixiang'
# this script is only used for the initiation of the database.
# after the database is initiated there will have to some cases in the database to be tested.
from database import *

print "Start Initiation of Database Schema"
print "Adding cases into the database"


Base.metadata.create_all(bind=engine)

# from database import *
# c = session.query(Clinic).filter_by(id=1).first()

#session.commit()

