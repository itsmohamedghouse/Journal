from models import User,JournalEntry
from datetime import datetime
def make_entry(user,content):
	entry=JournalEntry.create(content=content,author=user,timestamp=datetime.now())
	if entry == 1:
		print("entry saved")

def get_all_entries (user):
	entries=JournalEntry.select().where(JournalEntry.author == user)

	for entry in entries:
		print(entry.id,entry.timestamp,entry.content[:20],"...")

def get_entry_by_id(user):
	entries=JournalEntry.select().where(JournalEntry.author == user)
	if not entries:
		print("there are no journals")
	elif entries:
		entry_id=int(input("choose any entry id"))
		entry=JournalEntry.select().where(JournalEntry.id==entry_id).get()
		print("-"*20)
		print(entry.content)
		print("-"*20)

def register():
	username=input("enter user name-->")
	user=User.select().where(User.username == username)
	if user.exists():
		print("username exists :/")
		username=input("enter user name-->")


	password=input("create password-->")
	fullname=input("enter full name-->")
	entry=User.create(full_name=fullname,username=username,password=password)

def login():
	username=input("enter user name-->")
	password=input("enter password-->")
	user=User.select().where(User.username == username)

	if not user.exists():
		print("incorrect credentials :/")
		return 0

	if user.get().password == password:
		print("succesfully logged in\n")
		print(user.get().username)
		return user.get()

	else:
		print("fail\n")
		return 0
def delete_journal(user,id):
	entry=JournalEntry.select().where(JournalEntry.id==id).get()
	print("Delete the journal--",id)
	a=input("(y/n)-->")
	if a=="y":
		entry.delete_instance()
		print("Entry deleted")
	elif a=="n":
		print("Journal not deleted")
		return user.get()
