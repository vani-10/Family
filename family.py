#   Family Script
#       To perform CRUD operations in the process level
#
class familymember:           #This is a class holding family member objects 
	def setData(self,name,age):
		self.name=name
		self.age=age
	def displayData(self):
		print("Name is: ",self.name)
		print("Age is: ",self.age)			
		
print("Select operation.")
print("1.Add")
print("2.Display")
print("3.Update")
print("4.Delete")
family_list=[]               #contains list of family members (which has family objects)
while True:
	choice = input("Enter choice(1/2/3/4): ")
	
	if choice in ('1', '2', '3', '4'):

		if choice == '1':
			name=input("Enter the  name:")
			if type(name)!=str:
				raise TypeError("Name should be a string")
			elif name[0].isnumeric():
				print("Name can't begin with a number")
			elif len(name) < 0:
				print("minimum length should be at least one")
			name=input("Enter the name:")
			age=int(input("Enter the age:"))
			#create a object,fm of type family member.
			#set fm with values read above
			#append fm to family_list[]
			fm=familymember()
			fm.setData(name,age)
			family_list.append(fm)
			print("successfully added")

		elif choice =='2':
			found=False
			name2search=input("Enter the name to search:")
			#iterate through family_list for each and every family member
			#for each family member compare its name with name2search
			for eachmember in family_list:
				if(eachmember.name==name2search):
					print("Entry found...")
					print(eachmember.displayData()) 	
					found=True
					break
			if found==False:
				print("Name not found")
			

#		elif choice == '3':
#			key=input("Enter the name to search:")
#			searchData(f1,key)

			
			

	else:
		print("Invalid Input")