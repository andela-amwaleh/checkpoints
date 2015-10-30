from checkpoint1 import Space
import os




office =Space('OFFICE', 3, 1)
living =Space('LIVING', 3, 4)





def living_allocate(path):

	#if (os.path.isfile(path)):

		d =living.get_from_file(path)
		
		i = z = 0 
		print ("====================== List of allocation Living =========================\n")
		for x in d:
			
			if 'Y' in x and 'FELLOW' in x:
				
				s = living.allocate_room((x[0] + " "+ x[1]))
				print (s[:2])
				if s[0] == -1 : break
				z +=1
			i +=1
		print ("People allocated = {}".format(z))
		print ("\n")
		unallocated(d[i:], living.type_of_room)
	#else:
		#print('FILE NOT FOUND %s' %path)

def office_allocate(path):

	d = office.get_from_file(path)
	print ("====================== List of allocation  Office=========================\n")
	i = 0
	
	for x in d:
		
		s = office.allocate_room((x[0] + " "+ x[1]))
		print (s[:2])
		if s[0] == -1 : break
		
		i +=1

	print ("People allocated = {}".format(i))
	print ("\n"*3)

	unallocated(d[i:], office.type_of_room)
	

def unallocated(list,room_type):
	print ("====================== List of unallocated ({})=========================\n".format(room_type))
	for z in list:
		print ("{}  {: ^10}  {:_>10} ".format (z[0],z[1],z[2]))


while True :
	print (" Choose a Task \n")
	print ("1. Print room Allocations \n")
	print ("2. Allocate room\n") 
	print ("3. View room Occupants\n")
	print ("4. View room Status\n")
	try:
		task = int(raw_input("Insert room to allocate: "))
		if task in[1,2,3,4]: break
	except :
		print("ERROR: insert 1,2,3 or 4")
# --------------------Print room allocations

if task == 1 :
	while True :
		print ("Which Rooms ?\n")
		print ("1. Living \n")
		print ("2. Office\n")
		print ("3. Both\n")
		try:
			report = int(raw_input("Insert Space to print: "))
			if report in[1,2,3]: 
				if report == 1 : print(living.print_allocation())
				if report == 2 : print (office.print_allocation())
				if report == 3 : 
					print ("=+"*20)
					print("\n")
					print (living.print_allocation())
					print ("=+"*20)
					print("\n")
					print (office.print_allocation())

			break
		except :
			print("ERROR: insert 1,2 or 3")

# --------------------------------------Allocate rooms
if task == 2:

	while True :
		print("\n\n SECTION A: CHOOSE ROOM\n")
		print("0: Allocate Office")
		print("1: Allocate Living Space")
		print("2: Allocate both living and office")

		try:
			room_type = int(raw_input("Insert room to allocate: "))
			if room_type in[0,1,2]: 
				break

		except :
			print("ERROR: insert 0, 1, or 2")

	while True :
		print("\n SECTION B:CHOOSE INPUT METHOD \n")
		print("3: to insert Name directly")
		print("4: load names from a file")
		try:
			source  = int(raw_input("Input Method: "))
			if source in [3 ,4] : 
				break
				
		except :
			print("ERROR: insert 3 0r 4")


# ------------------------manual Input of names 

	if source == 3 :	
		while True:	
			
			inp = raw_input("Insert Name :")
			if inp !='':
				# exit code if input is 'exit'
				if inp == 'exit' : break
				# allocate room to person 
				if room_type == 0 :print (office.allocate_room(inp))
				if room_type == 1 : print (living.allocate_room(inp))
				if room_type == 2 : 
					print (office.allocate_room(inp))
					print (living.allocate_room(inp))
				# print allocated room
				
# -------------------------Loading Files from a file 

	if source == 4:
		try:
			file_path= raw_input(r"Insert full path of File :")

			if room_type == 0 : print (office_allocate(file_path))
			if room_type == 1 : print (living_allocate(file_path))
			if room_type == 2 : 
				print (office_allocate(file_path))
				print (living_allocate(file_path))
		except :
			print("ERROR: file does not exist")



# ----------------------View Room Cccupants
if task == 3 :
	while True :
		print ("Select Rooms ?\n")
		print ("1. Living \n")
		print ("2. Office\n")
		
		try:
			report = int(raw_input("Insert room type: "))

			room_num =raw_input("Insert room name: ").upper()

			if report in[1,2,3]: 
				print( "\n"*2)
				if report == 1 : 
					for x in living.get_room_occupants(room_num) :
						print( x )
				if report == 2 : 
					for x in office.get_room_occupants(room_num) :
						print (x)
				print( "\n"*2)
			break
		except :
			print("ERROR: insert 1 or 2")


# ----------------------- View room status
if task == 4:
	while True :
		print ("Select Rooms ?\n")
		print ("1. Living \n")
		print ("2. Office\n")
		print ("3.Both ")
		
		try:
			report = int(raw_input("Insert room type: "))
			if report in [1,2,3]: 
				print( "\n"*2)
				if report == 1 : 
					# print_status returns a list [empty_spaces, Summary of room status ] 
					# empty _spaces is a int 
					d=living.print_status()
					print ("Empty Spaces = {} ".format(d[0]))
					print (d[1])
						
				if report == 2 : 
					d=office.print_status()
					print ("Empty Spaces = {} ".format(d[0]))
					print (d[1])

				if report == 3:
					
					d=living.print_status()
					print ("Empty Living Spaces = {} ".format(d[0]))
					print (d[1])

					d=office.print_status()
					print ("Empty Office Spaces = {} ".format(d[0]))
					print (d[1])
				

				break
		except :
			print ("ERROR: insert 1 or 2")

	

		
	

