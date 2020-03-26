from peewee import *

db = SqliteDatabase('journal.db')

class User(Model):
	full_name = CharField()
	username = CharField() 
	password = CharField()

	class Meta:
		database = db # This model uses the "journal.db" database.
class JournalEntry(Model):
	author = ForeignKeyField(User, backref='entries')
	content = CharField()
	timestamp = TimestampField()

	class Meta:
		database = db # this model uses the "journal.db" database

if __name__=='__main__':
	# run only when models.py is executed
	db.connect()
	db.create_tables([User, JournalEntry])