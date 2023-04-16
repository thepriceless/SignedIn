import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import db.base as base
import db.models.user
import db.models.logstats

engine = create_engine(os.environ['DB_SIGNEDIN_URI'])
base.Base.metadata.create_all(engine)

#Session = sessionmaker(engine)
#session = Session()
