#!/usr/bin/python
import time
import getpass
import serial

def tst_motors(fd_serial):
 while(True):	
	menu = {}
	menu['1']="Motor 1"
	menu['2']="Motor 2"
	menu['3']="Motor 3"
	menu['4']="Motor 4"
	menu['0']="Select duty cycle"
	menu["-1"]="Exit test"

	select = {}
	select['0']=" "
	select["-1"]=" "
        select['1']=" "
        select['2']=" "
        select['3']=" "
        select['4']=" "

	print "Starting motors test...\n"
	
	while(True):
		m_options=menu.keys()
 		m_options.sort()
                s_options=select.keys()
                s_options.sort()

#MENU: Select Motor
  		print "*************************************"
  		print "***         Select Motor          ***"
		for entry in m_options:
      			print "    ", entry, " --> ", menu[entry], select[entry]

  		print "***                               ***"
  		print "*************************************\n"
# Select option
		selection=raw_input("Please select an option: ")
		if selection == '0':
			flag = False
		      	for entry in s_options:
				if select[entry] == "X":
					flag = True
					break
			if flag == True:
				break				
			print "At lease one motor should be selected"	
		elif selection == '1':
      		      if select['1']=="X":
			 select['1']=" "
		      else:
			 select['1']="X"
  		elif selection == '2':
                      if select['2']=="X":
                         select['2']=" "
                      else:
                         select['2']="X"
  		elif selection == '3':
                      if select['3']=="X":
                         select['3']=" "
                      else:
                         select['3']="X"

		elif selection == '4':
                      if select['4']=="X":
                         select['4']=" "
                      else:
                         select['4']="X"
	        elif selection == "-1":
			return
  		else:
      			print "Unknown Option Selected!"
	while(True):
		selection=raw_input("Select duty cycle 0-100% (-1 to return): ")
		if selection == "-1":
			break
		if selection.find(".") == -1:
			selection = selection + ".0"

		stof = float(selection)
		if stof>100:
			selection = "100.0"
		if stof<0:
			selection = "0.0"		
                for entry in s_options:
			if entry == "-1" or entry == '0':
				continue
			if select[entry] == "X":
                            selection = selection + ":" + entry

		fd_serial.write("2\n\0")
		fd_serial.write(selection + "\n")
		time.sleep(0.1)
		if(fd_serial.inWaiting() != 0):
	        	receive = fd_serial.readline()
			if receive == "OK\n":
				print("Done.")
			else:
				print("Error... Cannot be changed the duty cycle.\n\n")
		else:
			print("ERROR... Cannot be changed the duty cycle\n\n")
	
