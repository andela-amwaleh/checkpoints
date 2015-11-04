from checkpoint1 import Space
import os

# office reads room allocation from file 'rooms.txt'
office = Space(6)
# living work space is generated by inputing the parameters
living = Space(4, 'Living', 10)


def living_allocate(path):

    if (os.path.isfile(path)):

        destination = living.get_from_file(path)
        # intitialize counter to check index reached
        i = 0
        # intialize counter to check how many rooms have been allocated
        z = 0

        print("=="*10 + " List of allocation Living " + "=="*10 + "\n")

        for x in destination:
            if 'Y' in x and 'FELLOW' in x:
                space = living.allocate_room((x[0] + " " + x[1]))
                print(space[:2])
                # if the rooms are full break the loop
                if space[0] == -1:
                    break
                # add to allocated counter
                z += 1
            i += 1

        print("People allocated = {}".format(z))
        print("\n")
        # Pass the unallocated list for printing
        unallocated(destination[i:], living.type_of_room)

    else:
        print('FILE NOT FOUND %s' % path)


def office_allocate(path):

    d = office.get_from_file(path)
    print("=="*10 + " List of allocation Office " + "=="*10 + "\n")
    # Introduce a counter to know how many elements have been processed
    i = 0
    for x in d:
        s = office.allocate_room((x[0] + " " + x[1]))
        print(s[:2])
        if s[0] == -1:
            break

        i += 1

    print("People allocated = {}".format(i))
    print("\n"*3)

    # Using i get the remining unprocessed list
    unallocated(d[i:], office.type_of_room)


def unallocated(list, room_type):
    print("==" * 10 + "List of unallocated ({})" + "=="*10 + "\n".format(
        room_type))
    for z in list:
        print("{}  {: ^10}  {:_>10} ".format(z[0], z[1], z[2]))


while True:
    print(" CHOOSE A TASK \n")
    print("1. Print room Allocations \n")
    print("2. Allocate room\n")
    print("3. View room Occupants\n")
    print("4. View room Status\n")
    print("0. to exit\n")

    try:
        task = int(raw_input("Insert room to allocate: "))
        if task == 0:
            exit()

        if task in [1, 2, 3, 4, 0]:
            break

    except:
        print("ERROR: insert 1,2,3 or 4")

# --------------------Print room allocations
if task == 'exit':
    exit

if task == 1:
    while True:
        print("Which Rooms ?\n")
        print("1. Living \n")
        print("2. Office\n")
        print("3. Both\n")
        print("0. Exit\n")
        try:
            report = int(raw_input("Insert Space to print: "))
            if report in[1, 2, 3, 0]:
                if report == 0:
                    exit
                if report == 1:
                    print(living.print_allocation())
                if report == 2:
                    print(office.print_allocation())
                if report == 3:
                    print("=+"*20)
                    print("\n")
                    print(living.print_allocation())
                    print("=+"*20)
                    print("\n")
                    print(office.print_allocation())

            break
        except:
            print("ERROR: insert 1,2 or 3")

# --------------------------------------Allocate rooms
if task == 2:

    while True:
        print("\n\n SECTION A: CHOOSE ROOM\n")
        print("0: Allocate Office")
        print("1: Allocate Living Space")
        print("2: Allocate both living and office")
        print("3: Exit\n")

        try:
            room_type = int(raw_input("Insert room to allocate: "))
            if room_type in[0, 1, 2, 3]:
                break

        except:
            print("ERROR: insert 0, 1, or 2")

    while True:
        if room_type == 3:
            exit()

        print("\n SECTION B:CHOOSE INPUT METHOD \n")
        print("3: to insert Name directly")
        print("4: load names from a file")

        try:
            source = int(raw_input("Input Method: "))
            if source in [3, 4]:
                break
        except:
            print("ERROR: insert 3 0r 4")

    # ------------------------manual Input of names
    if source == 3:
        while True:

            inp = raw_input("Insert Name or exit to stop :")
            if inp != '':
                # exit code if input is 'exit'
                if inp == 'exit':
                    break
                # allocate room to person
                if room_type == 0:
                    print(office.allocate_room(inp))
                if room_type == 1:
                    print(living.allocate_room(inp))
                if room_type == 2:
                    print(office.allocate_room(inp))
                    print(living.allocate_room(inp))
                # print allocated room

    # -------------------------Loading Files from a file
    if source == 4:
        try:
            file_path = raw_input(r"Insert full path of File :")

            if room_type == 0:
                print(office_allocate(file_path))
            if room_type == 1:
                print(living_allocate(file_path))
            if room_type == 2:
                print(office_allocate(file_path))
                print(living_allocate(file_path))
        except:
            print("ERROR: file does not exist")

# ----------------------View Room Cccupants
if task == 3:
    while True:
        print("Select Rooms ?\n")
        print("1. Living \n")
        print("2. Office\n")
        print("0. exit\n")

        try:
            report = int(raw_input("Insert room type: "))
            if report == 0:
                break

            room_num = raw_input("Insert room name: ")

            if report in[1, 2, 0]:
                print("\n"*2)

                if report == 1:
                    for x in living.get_room_occupants(room_num):
                        print(x)
                if report == 2:
                    for x in office.get_room_occupants(room_num):
                        print(x)
                print("\n"*2)
            break
        except:
            print("ERROR: insert 1 or 2")

# ----------------------- View room status
if task == 4:
    while True:
        print("Select Rooms ?\n")
        print("1. Living \n")
        print("2. Office\n")
        print("3. Both\n")
        print("0. exit")

        try:
            report = int(raw_input("Insert room type: "))
            if report in [0, 1, 2, 3]:
                print("\n"*2)
                if report == 0:
                    break

                if report == 1:
                    # print_status returns a list [empty_spaces, Summary of room status ]
                    # empty _spaces is a int
                    d = living.print_status()
                    print("Empty Spaces = {} ".format(d[0]))
                    print(d[1])

                if report == 2:
                    d = office.print_status()
                    print("Empty Spaces = {} ".format(d[0]))
                    print(d[1])

                if report == 3:
                    d = living.print_status()
                    print("Empty Living Spaces = {} ".format(d[0]))
                    print(d[1])

                    d = office.print_status()
                    print("Empty Office Spaces = {} ".format(d[0]))
                    print(d[1])

                break
        except:
            print("ERROR: insert 1 or 2")
