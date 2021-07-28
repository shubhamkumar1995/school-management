import os, getpass, json
from adminpanel import AdminPanel
from login import PasswordReset


class FacultyPanel(AdminPanel):
	"""docstring for Faculty Panel"""
	
	def __init__(self, checkLogin):
		
		super(AdminPanel, self).__init__()
		os.system('clear')
		while True:
			if checkLogin == True:
				
				print("\n\n*******Welcome to Faculty Panel*********")
				#print("\n\n Welcome {}".format(user))
				print("\n\n1. View Your Profile\n2. Change Password")
				print("3. Add Student Record\n4. View all Record of Student\n5. Delete Student Record\n6. Exit")
				facultyChoice = int(input("\n\n Enter Your Choice:  "))

				if facultyChoice == 1:
					self.ViewProfile()
				elif facultyChoice == 2:
					print("\n\n*******Change Password **********\n\n")
					PasswordReset()

				elif facultyChoice == 3:
					self.AddStudentsRecords()
				elif facultyChoice == 4:
					self.ViewStudentsRecords()
				elif facultyChoice == 5:
					self.DeleteStudentsRecords()
				elif facultyChoice == 6:
					exit()

	def ViewProfile(self):
		""" This Function is used to see the faculty records.
		 """
		print("\n\n ******** My Profile ********\n\n ")

		with open('facultyrecords.json', 'r') as f:
			facultyRecords = json.loads(f.read())

			viewPerson = input("\n Enter either your 'UserName' or 'Name': ")

			#print(facultyRecords)
			for i in facultyRecords['faculty-records']:
				if i['Username'] == viewPerson or i['Name'] == viewPerson:
					i['Password'] = "*******"
					print("\n Username: ",i['Username'])
					print(" Password: ",i['Password'])
					print(" Name: ",i['Name'])
					print(" Address: ",i['Address'])
					print(" Qualification: ",i['Qualification'])
					print(" Subjects: ",i['Subjects'])
					break
			else:
				print("This name does not exist ")

	def UpdatePassword(self):
		print("Update Feature is under development ")


if __name__ == '__main__':
	
	checkLogin = True

	FacultyObject = FacultyPanel(checkLogin)