from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean
engine = create_engine('postgresql://postgres:postgres@localhost:5432/running', echo = False)
meta = MetaData()

Logging = Table(
   'gate_test', meta, 
   Column('index', Integer, primary_key = True), 
   Column('gate_id', Integer), 
   Column('tag_number', String),
   Column('timestamp', String),
   Column('check', Boolean)
)

meta.create_all(engine)
