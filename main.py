from app import *
while True:
	print("choose option \n 1.register\n 2.login\n 3.exit")
	choice=input("-->")
	print("-"*20)
	if choice == "1":
		register()
	elif choice=="2":
		user=login()
		t= True
		while t:
			print("what would you like to do\n 1.create entry\n 2.check entry\n 3.delete entry\n 4.logout")
			choice1=input("-->")	
			if choice1=="1":
				if user:
					content=input("write below \n-----------\n")
					make_entry(user,content)
				else:
					continue

			elif choice1=="2":
				# user=login()
				if user:
					get_all_entries(user)
					# entry_id=input("choose any entry id")
					get_entry_by_id(user)
				else:
					continue
			elif choice1=="3":
				if user:
					get_all_entries(user)
					entry_id=input("choose entry id which you want to be deleted-->")
					get_entry_by_id(entry_id)
					delete_journal(user,entry_id)
				else:
					continue
			elif choice1=="4":
				t= False
	elif choice=="3":
		exit(0)