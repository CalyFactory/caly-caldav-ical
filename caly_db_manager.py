from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pprint

import caly_db_schema

class CaldavDBmanager:
	def __init__(self):
		# If echo=True, You can see a log about tutorial.db
		self.engine = create_engine('sqlite:///tutorial.db', echo=False)
		caly_db_schema.Base.metadata.bind = self.engine

		self.DBSession = sessionmaker(bind=self.engine)
		self.session = self.DBSession()
		#self.insert()
		self.select()


	## CRUD
	def insert(self):
		new_person = caly_db_schema.Person(name='new person7')
		self.session.add(new_person)
		self.session.commit()

		new_person2 = caly_db_schema.Person(name='new person8')
		self.session.add(new_person2)
		self.session.commit()

		new_person3 = caly_db_schema.Person(name='new person9')
		self.session.add(new_person3)
		self.session.commit()

		new_address = caly_db_schema.Address(post_code='000000', person=new_person)
		self.session.add(new_address)
		self.session.commit()

		new_address2 = caly_db_schema.Address(post_code='000001', person=new_person2)
		self.session.add(new_address2)
		self.session.commit()

		new_address3 = caly_db_schema.Address(post_code='000002', person=new_person3)
		self.session.add(new_address3)
		self.session.commit()

	def select(self):
		people = self.session.query(caly_db_schema.Person).all()
		for person in people:
			print(person.name)

		#pp = pprint.PrettyPrinter(width=100, compact=True)
		#pp.pprint(people)
	def update(self):
		pass

	def delete(self):
		pass


db_client = CaldavDBmanager()