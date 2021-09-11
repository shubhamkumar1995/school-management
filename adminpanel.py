import os, getpass, json
from login import AdminPasswordReset

class AdminPanel:
	"""docstring for AdminPanel"""
	
	def __init__(self, checkLogin):
		
		#super(AdminPanel, self).__init__()
		os.system('clear')
		while True:
			if checkLogin == True:
				
				print("\n\n*******Welcome to Admin Panel*********")
				print("\n\n1. View Admin Profile\n2. Change Password\n3. Add Faculty Record\n4. View all Record of Faculty")
				print("5. Delete Faculty Record\n6. Add Student Record\n7. View all Record of Student\n8. Delete Student Record")
				print("9. Exit")
				adminChoice = int(input("\n\n Enter Your Choice:  "))

				if adminChoice == 1:
					self.ViewAdminProfile()
				elif adminChoice == 2:
					print("\n\n ****** Change Password******* \n\n")
					AdminPasswordReset()
				elif adminChoice == 3:
					self.AddFacultyRecords()
				elif adminChoice == 4:
					self.ViewFacultyRecords()
				elif adminChoice == 5:
					self.DeleteFacultyRecords()
				elif adminChoice == 6:
					self.AddStudentsRecords()
				elif adminChoice == 7:
					self.ViewStudentsRecords()
				elif adminChoice == 8:
					self.DeleteStudentsRecords()
				elif adminChoice == 9:
					exit()
	

	def ViewAdminProfile(self):
		""" This Function is used to see the faculty records.
		 """
		print("\n\n ******** My Profile ********\n\n ")

		with open('adminlogin.json', 'r') as f:
			adminRecords = json.loads(f.read())

			for i in adminRecords['admin-details']:
				if i['Username'] == 'admin':
					i['Password'] = "*******"
					print("\n Username: ",i['Username'])
					print(" Password: ",i['Password'])
					print(" Name: ",i['Name'])
					print(" Address: ",i['Address'])
					print(" Qualification: ",i['Qualification'])
					print(" Experience: ",i['Experience'])
					print(" Designation: ",i['Designation'])
					print("\n\n------------------------------------------")
					break

	def AddFacultyRecords(self):
		os.system('clear')
		"""
		Admin will create the login and password of faculties with the faculty name,
		The data will get stores in the logincredentials.txt file.
		"""
		while True:
			print("\n\n******* Add Faculty Records******* \n\n")
			facultyUserName = input("Create a username of Faculty (must be unique): ")
			facultyPassword = input("\nCreate a Password: ")
			print("\n\n Note: Secondary password will not be visible while entering:\n ")
			facultyPassword2 = getpass.getpass("Re-Enter the password again:  ") 

			if facultyPassword == facultyPassword2:
				print("Password Matching")
				os.system('clear')
				print("\n\n       ********** Faculty Details Form ************\n\n\n")
				print(" username : {}".format(facultyUserName))
				facultyName = input("\n\n\n Enter Faculty's Name:  ")
				facultyName = facultyName.title()

				facultyAddr = input("\n Enter the Address(city): ")
				facultyAddr = facultyAddr.title()
				
				facultyQualification = input("\n Enter the Qualification: ")
				facultyQualification = facultyQualification.title()

				facultySubjects = input("\n Enter the subjects to be assigned: ")
				facultySubjects = facultySubjects.title()

				facultyRecords1 = { "faculty-records" : [
				{ "Username" : facultyUserName,
				"Password" : facultyPassword, 
				"Name" : facultyName, 
				"Address" : facultyAddr, 
				"Qualification" : facultyQualification, 
				"Subjects" : facultySubjects

				}]

				}

				facultyRecords2 = {
				"Username" : facultyUserName,
				"Password" : facultyPassword, 
				"Name" : facultyName, 
				"Address" : facultyAddr, 
				"Qualification" : facultyQualification, 
				"Subjects" : facultySubjects
				}

				if os.stat("facultyrecords.json").st_size == 0:
					with open("facultyrecords.json", 'w') as f:
						records = json.dumps(facultyRecords1, indent =4)
						f.write(records)
						print("\n\n Data Saved Successfully")
				else:
					with open("facultyrecords.json", "r+") as file:		#append the new faculty data in the existing json array.
						parsed_data = json.load(file)
						parsed_data["faculty-records"].append(facultyRecords2)
						file.seek(0)
						json.dump(parsed_data, file, indent = 4)
						print("\n\n Data Saved Successfully")

				return False
			else:
				print("\n Password are not matching, Re-Enter it again")
				continue



		
	def ViewFacultyRecords(self):

		""" This Function is used to see the faculty records.
		 """
		print("\n\n ******** View Faculty Data ********\n\n ")

		with open('facultyrecords.json', 'r') as f:
			facultyRecords = json.loads(f.read())

		viewFacultyData = int(input("\nSelect the following choices:\n\n1. View All Faculty Data\n2. View Specific person data:  "))
		if viewFacultyData == 1:

			for i in facultyRecords['faculty-records']:
				i['Password'] = "*******"
				print("\n",i, "\n ")

		elif viewFacultyData == 2:

			viewPerson = input("\n Enter either 'UserName' or 'Name' of the faculty: ")

			#print(facultyRecords)
			for i in facultyRecords['faculty-records']:
				if i['Username'] == viewPerson or i['Name'] == viewPerson:
					i['Password'] = "*******"
					print("\n",i)
	
	

	def DeleteFacultyRecords(self):
		
		print("\n\n ********* Delete Faculty's Data *********\n\n")

		deleteFacultyData = input("Enter the name of the Faculty:  ")
		deleteFacultyData = deleteFacultyData.title()


		if os.stat("facultyrecords.json").st_size == 0:
			print("\n Alert : No Faculty Records Available")
		else:
			with open("facultyrecords.json", "r+") as file:
				file_data = json.load(file)
				#print(file_data)
				
				for i in file_data["faculty-records"]:
					if i['Name'] == deleteFacultyData:
						
						file_data["faculty-records"].remove(i)
						#print(file_data)
						file = open('facultyrecords.json', mode='w+')
						json.dump(file_data, file, indent =4)
						print("\n\n Data Deleted Successfully")
						file.close()
						break

				else:
					print(f"\n Faculty of name {deleteFacultyData} does not exist")


	

	def AddStudentsRecords(self):
		
		os.system('clear')
		"""This function is used to append the new student data in the json array. """
		add_more_data = 'y'

		while add_more_data == 'y':

			print("\n\n *******  Add Student Data ***********\n\n ")
			studentId = int(input("Enter the student Id.\n(Must be in a Integer Format): "))
			studentName = input("Enter the name of the Student: ")
			studentName = studentName.title()

			address = input("Enter the Address (Name of city only): ")
			courseName = input("Enter the Course Name: ")
			courseDuration = int(input("Enter the course duration\n(Only enter the no. of days in interger format): "))

			StudentData1 ={ "student-data" : #This will be used if the file is blank
				[
					{
					"Name" : studentName,
					"StudentID" : studentId,
					"Address" : address,
					"Course Name" : courseName,
					"Course Duration" : courseDuration  

					},
				]
			}

			StudentData2 = {
			"Name" : studentName,
			"StudentID" : studentId,
			"Address" : address,
			"Course Name" : courseName,
			"Course Duration" : courseDuration

			}

			if os.stat("studentdata.json").st_size == 0:  				#Checks if file is empty!.
				with open("studentdata.json", "w") as outfile:
			 		#outfile.write("[\n\n]")
			 		json_object = json.dumps(StudentData1, indent =4)
			 		outfile.write(json_object)
			else:
				with open("studentdata.json", "r+") as file:		#append the new student data in the existing json array.
					new_data = json.load(file)
					new_data["student-data"].append(StudentData2)
					file.seek(0)
					json.dump(new_data, file, indent = 4)

			add_more_data == input("Do you want to add more students data? y/n:  ")
			
			if add_more_data.lower() == 'y':
				continue
			else:
				break
				exit()

	

	def ViewStudentsRecords(self):
		#print("View Students Records\n This feature is under development.")
		studentList = []
		
		print("\n\n******* Students Record *************\n\n")
		
		with open('studentdata.json', 'r') as openfile:
			json_object = json.loads(openfile.read())
		
			
			for i in json_object['student-data']:
				print("\n",i, "\n")



	def DeleteStudentsRecords(self):
		""" To get and delete data from JSON Array. """



		print("\n\n ********* Delete Student Data *********\n\n")

		deleteData = input("Enter the name of the Student:  ")
		deleteData = deleteData.title()


		if os.stat("studentdata.json").st_size == 0:
			print("\n Alert : No Student Records Available")
		else:
			with open("studentdata.json", "r+") as file:
				file_data = json.load(file)
				#print(file_data)
				
				for i in file_data["student-data"]:
					if i['Name'] == deleteData:
						
						file_data["student-data"].remove(i)
						#print(file_data)
						file = open('studentdata.json', mode='w+')
						json.dump(file_data, file, indent =4)
						print("\n\n Data Deleted Successfully")
						file.close()
						break

				else:
					print(f"\n Student of name {deleteData} does not exist")



if __name__ == '__main__':
	
	checkLogin = True

	adminObject = AdminPanel(checkLogin)



