import os
from login import adminlogin, facultylogin
from adminpanel import AdminPanel
from facultypanel import FacultyPanel

def menu():
	print("\n\n********** Welcome to Narayana Tech House **********")
	print("\n\n 1. Admin Portal\n 2. Faculty Portal: ")

	userChoice = int(input("\n\n Enter your choice:  "))

	if userChoice == 1:
		os.system('clear')
		print("\n\n******** Welcome to Admin Panel **********\n\n")
		checkLogin = adminlogin()
		AdminObject = AdminPanel(checkLogin)
		AdminPanel.AddFacultyRecord(self)
	

	if userChoice == 2:
		os.system('clear')
		print("\n\n******** Welcome to Faculty Panel **********\n\n")
		checkLogin = facultylogin()
		FacultyObject = FacultyPanel(checkLogin)
		
	

	# if userChoice == 3:
	# 	os.system('clear')
	# 	print("\n\n******** Welcome to Student Panel **********\n\n")
	# 	checkLogin = StudentLogin()

if __name__ == '__main__':
	menu()