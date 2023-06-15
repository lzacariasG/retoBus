import os
import psycopg2 

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine
psycopg2.connect("postgresql://jonathan:admin@localhost:5432/bdBous ")
