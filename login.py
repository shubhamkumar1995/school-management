import getpass, os, json


def adminlogin():

	def IfAdminTrue(username, password):

		with open('adminlogin.json') as file:
			parsed = json.load(file)

			for i in parsed["admin-details"]:
				if username == "admin" and i['Password'] == password:
					return True

			else:
				return False
	# IfLoginTrue Function ends here....
	#facultyLogin Body Starts.....

	maximum = 2
	i = 0
	
	while i<3:

		print("\n *********Admin Login Page *********\n\n ")

		username = input("Enter your UserName:  ")

		print("\n Note: Password will not be visible while entering\n")
		password = getpass.getpass()


		loginCheck = IfAdminTrue(username, password)	# calling function to validate.	
				
		if loginCheck == True:
			print("Login Successful")
			return True

		else:
			print("\n Invalid Login or Password")
			print("\n--------------------------------")
			count = maximum -i
			if count>0:
				print(f"\n You have {count} attempts left ")
					
			if i==2:
				print("\n\nYou have used your all attempts")
				reset = input("Do you want to reset your Password?   y/n: ")
				if reset.lower() == 'y':
					print("\n ********* Reset Password *********\n\n ")
					AdminPasswordReset()
					exit()
				else:
					exit()
			else:
				i=i+1


def AdminPasswordReset():

	print("\n \n ")

	resetUsername = input("Enter your UserName:  ")

	print("\n Note: Password will not be visible while entering\n")
	resetPassword1 = getpass.getpass("Enter your New Password:  ")

	resetPassword2 = getpass.getpass("Re-Enter your New Password:  ")
	
	if resetPassword1 == resetPassword2:

		with open('adminlogin.json', "r+") as file:
			parsed = json.load(file)
		
		for i in parsed["admin-details"]:
			if i['Username'] == resetUsername:
				
				i['Password'] = resetPassword1
				file = open('adminlogin.json', mode='w+')
				json.dump(parsed, file, indent =4)
				print("\n\n Password Changed Successfully")
				file.close()
				break

		else:
			print("\n\nUsename not found in our Database")
			exit()
	else: 
		print("\n Entered Password(s) Not Matching")
		exit()



#------------------------Admin Work Ends Here -----------------------
def facultylogin():

	def IfLoginTrue(username, password):

		with open('facultyrecords.json') as file:
			parsed = json.load(file)
			
			for i in parsed["faculty-records"]:
				if i['Username'] == username and i['Password'] == password:
					return True

			else:
				return False
	# IfLoginTrue Function ends here....
	#facultyLogin Body Starts.....

	maximum = 2
	i = 0
	
	while i<3:

		print("\n ********* Faculty Login *********\n\n ")

		username = input("Enter your UserName:  ")

		print("\n Note: Password will not be visible while entering\n")
		password = getpass.getpass()


		loginCheck = IfLoginTrue(username, password)	# calling function to validate.	
				
		if loginCheck == True:
			print("Login Successful")
			return True

		else:
			print("\n Invalid Login or Password")
			print("\n--------------------------------")
			count = maximum -i
			if count>0:
				print(f"\n You have {count} attempts left ")
					
			if i==2:
				print("\n\nYou have used your all attempts")
				reset = input("Do you want to reset your Password?   y/n: ")
				if reset.lower() == 'y':
					print("\n ********* Reset Password *********\n\n ")
					PasswordReset()
					exit()
				else:
					exit()
			else:
				i=i+1
				#continue
		
#------------------------------------------------------------------------------- 			

def PasswordReset():

	print("\n\n ")

	resetUsername = input("Enter your UserName:  ")

	print("\n Note: Password will not be visible while entering\n")
	resetPassword1 = getpass.getpass("Enter your New Password:  ")

	resetPassword2 = getpass.getpass("Re-Enter your New Password:  ")
	
	if resetPassword1 == resetPassword2:

		with open('facultyrecords.json', "r+") as file:
			parsed = json.load(file)
		
		for i in parsed["faculty-records"]:
			if i['Username'] == resetUsername:
				
				i['Password'] = resetPassword1
				file = open('facultyrecords.json', mode='w+')
				json.dump(parsed, file, indent =4)
				print("\n\n Password Changed Successfully")
				file.close()
				break

		else:
			print("\n\nUsename not found in our Database")
			exit()
	else: 
		print("\n Entered Password(s) Not Matching")
		exit()




if __name__ == '__main__':
	pass

	# checkLogin = AdminLogin()
	# print(checkLogin)
	#facultylogin()
	#PasswordReset()
	adminlogin()




















	'''
	def login():

	""" This function is used for Login, It get the data from the credentials file and compare it. 
	Password on this function is fully secured (not visible on the screen), Please do not make any changes in this function."""
	
	with open('loginCredentials.txt') as log:
		credentials = log.readlines()
		print(credentials)

	credentialsDictionary = {}

	for i in credentials:
		parsed = i.split(",")
		
		keys, values = parsed[0], parsed[1]
		credentialsDictionary[keys] = values


	username = input("Enter the UserName: ")
	username = username.lower()
	password = getpass.getpass()

	if username.isalpha():
		
		for i in credentialsDictionary:
			if i== username and credentialsDictionary[i] == password:
				print("\nLogin Successful")
				return True
				break
		else:
			print("\n\n Alert: Username or Password Invalid")
			return False
	else:
		print("Username must be alphabetical")
		return False
	'''
