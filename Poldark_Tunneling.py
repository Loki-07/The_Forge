#! /usr/bin/python

def main_title():
	print("     _ __        _,.---._                                  ,---.                     ,--.-.,-.  ")
	print("  .-`.' ,`.    ,-.' , -  `.      _.-.       _,..---._    .--.'  \       .-.,.---.   /==/- |\  \ ")
	print(" /==/, -   \  /==/_,  ,  - \   .-,.'|     /==/,   -  \   \==\-/\ \     /==/  `   \  |==|_ `/_ / ")
	print("|==| _ .=. | |==|   .=.     | |==|, |     |==|   _   _\  /==/-|_\ |   |==|-, .=., | |==| ,   /  ")
	print("|==| , '=',| |==|_ : ;=:  - | |==|- |     |==|  .=.   |  \==\,   - \  |==|   '='  / |==|-  .|   ")
	print("|==|-  '..'  |==| , '='     | |==|, |     |==|,|   | -|  /==/ -   ,|  |==|- ,   .'  |==| _ , \  ")
	print("|==|,  |      \==\ -    ,_ /  |==|- `-._  |==|  '='   / /==/-  /\ - \ |==|_  . ,'.  /==/  '\  | ")
	print("/==/ - |       '.='. -   .'   /==/ - , ,/ |==|-,   _`/  \==\ _.\=\.-' /==/  /\ ,  ) \==\ /\=\.' ")
	print("`--`---'         `--`--''     `--`-----'  `-.`.____.'    `--`         `--`-`--`--'   `--`       ")
	print("\n                      Your Planner for all your Tunneling needs")
	print("\n")
	print("\n                              Created in Lokis Forge")
	print("                                lokis-notebook.org")
	print("\n")


def ssh_tunnel1():
	ssh=True
	while ssh:
#first target machine and 2nd Target Machine
		ip1=raw_input("\n What is the IP of the 1st Target Machine?")
		Lport1=raw_input("\n Enter the desired Listening port for the 1st target machine?")
		ip2=raw_input("\n What is the IP of the 2nd Target Machine?")
		print(" ssh %s" %(ip1))
		print(" ssh %s -L %s:%s:22" %(ip1, Lport1, ip2))
		
		###This is the Yes/No question to continue in the Function
		cont=True
		while True:
			cont=raw_input("Would you like to add another Box (y,n)")
			if cont == "y":
				print("Enter the 3rd Target Set next")
				break
			elif cont == "n":
				print("Returning to Main Menu")
				return False
				
#Target Number 3 Starts Here				
		Lport2=raw_input("\n Enter the desired Listening port for the 2nd target machine?")
		ip3=raw_input("\n What is the IP of the 3rd Target Machine?")
		print(" ssh 127.0.0.0.1 -p %s -L %s:%s:22" %(Lport1,Lport2,ip3))
		
		###This is the Yes/No question to continue in the Function
		cont=True
		while True:
			cont=raw_input(" Would you like to add another Box (y,n)")
			if cont == "y":
				print(" Enter the 3rd Target Set next")
				break
			elif cont == "n":
				print(" Returning to Main Menu")
				return False
				
#Target Number 4 Starts Here				
		Lport3=raw_input("\n Enter the desired Listening port for the 3nd target machine?")
		ip4=raw_input("\n What is the IP of the 4th Target Machine?")
		print(" ssh 127.0.0.0.1 -p %s -L %s:%s:22" %(Lport2,Lport3,ip4))

#final String before breacking to the Main menu
		cont=True
		while True:
			cont=raw_input("Display all lines in sequence? (y,n)")
			if cont == "y":
				print(" ssh %s" %(ip1))
				print(" ssh %s -L %s:%s:22" %(ip1, Lport1, ip2))
				print(" ssh 127.0.0.0.1 -p %s -L %s:%s:22" %(Lport1,Lport2,ip3))
				print(" ssh 127.0.0.0.1 -p %s -L %s:%s:22" %(Lport2,Lport3,ip4))
				display=True
				while True:
					display=raw_input(" Display Visual Representation? (y,n)")
					if display =="y":
						print("ATTACK BOX             BOX1              BOX2                BOX3              BOX4")
						print("YOUR IP          %s         %s        %s         %s"%(ip1, ip2, ip3, ip4))
						print(" ---------           ---------          ---------          ---------          --------- ") 
						print("|         |         |         |        |         |        |         |        |         |")  
						print("|        ----------->22       |        |         |        |         |        |         |") 
						print("|    >5555====================--------->%s       |        |         |        |         |"%(Lport1))  
						print("|    >6666=======================================--------->%s       |        |         |"%(Lport2))  
						print("|    >7777==========================================================--------->%s       |"%(Lport3)) 
						print("|         |         |         |        |         |        |         |        |         |") 
						print("|         |         |         |        |         |        |         |        |         |") 
						print("|         |         |         |        |         |        |         |        |         |") 
						print("|_________|         |_________|        |_________|        |_________|        |_________|") 
						print("ssh %s" %(ip1))
						print("ssh %s -L %s:%s:22" %(ip1, Lport1, ip2))
						print("ssh 127.0.0.0.1 -p %s -L %s:%s:22" %(Lport1,Lport2,ip3))
						print("ssh 127.0.0.0.1 -p %s -L %s:%s:22" %(Lport2,Lport3,ip4))
						#####This is how you ensure the user is ready to continue with a key stroke
						try:
							input(" Press any key to return to the main menu")
						except SyntaxError:
							pass
						return False
						
					elif display == "n":
						print(" Returning to Main Menu")
						print("\n")
						print("\n")
						return False
			elif cont == "n":
				print(" Returning to Main Menu")
				return False


def ssh_tunnel1_Multiport():
	ssh=True
	while ssh:
#This will give the command for 2 connections, one to open the SSH tunnel the second to open a tunnel to a specific port
		print("First we will establish the connection to the first machine")
		ip1=raw_input("\n What is the IP of the 1st Target Machine?")
		Lport1=raw_input("\n Enter the desired Listening port for the 1st target machine?")
		ip2=raw_input("\n What is the IP of the 2nd Target Machine?")
		print("\n")
		print(" Next we will enter the ports we wish to establish connections to the 2nd machine on")
		tport1=raw_input("\n Enter the target port you wish to use (such as port 80)")
		Lport2=raw_input("\n Enter the desired Listening port for the 2nd target machine?")
		print(" ssh %s" %(ip1))
		print(" ssh %s -L %s:%s:22" %(ip1, Lport1, ip2))
		print(" ssh %s -L %s:%s:22 -L %s:%s:%s" %(ip1, Lport1, ip2, Lport2, ip2, tport1))
		print("\n Note: You can add additional ports by replicating the second -L line. Such as ssh %s -L %s:%s:22 -L %s:%s:%s -L <New Listening Port>%s:<New Target Port>"%(ip1, Lport1, ip2, Lport2, ip2, tport1, ip2))
		print("\n To access this port use your normal port use program (IE Browser for port 80) pointed at %s and the Listening Port 2 %s" %(ip1, Lport2))
		print(" For Example: In a web Browser - %s:%s"%(ip1, Lport2))
		print("\n")
		print("\n")	
		
		#####This is how you ensure the user is ready to continue with a key stroke
		try:
			input(" Press any key to return to the main menu")
		except SyntaxError:
			pass
		break

def ssh_reverse_tunnel():
	ssh=True
	while ssh:
#This will give the command for 2 connections, one to open the SSH tunnel the second to open a tunnel to a specific port
		print("First we will establish the connection to the first machine")
		Lport1=raw_input("\n What is the listening port that will allow you to get to the Target Machine (should be a listener on your Machine). You will have already established this connection")
		Lport2=raw_input("\n What is the Port you want to send traffic back on from the Target Machine?")
		Rport2=raw_input("\n What is the listening port you would like to receive the tunnel on?")
		print("ssh 127.0.0.1 -p %s -R %s:127.0.0.1:%s" %(Lport1, Lport2, Rport2))
		
		#####This is how you ensure the user is ready to continue with a key stroke
		try:
			input("Press any key to return to the main menu")
		except SyntaxError:
			pass
		break		
				
def windows_port_forward():
	portfwd=True
	while portfwd:
		print("Windows port forwarding will allow you to push traffic through a Windows machine in a similiar manner to SSH Tunneling.")
		inport=raw_input("\n What is the Port on the Forwarding Machine you will use?")
		listenaddr=raw_input("\n What is the Windows Machine IP?")
		connectaddr=raw_input("\n What is the target that you traffic will be forwarded to?")
		connectport=raw_input("\n WHat is the connection port you wish your traffic to arrive at?")
		print("\n")
		print("netsh interface portproxy add v4tov4 listenport=%s listenaddress=%s connectaddress=%s connectport=%s" %(inport, listenaddr, connectaddr,connectport))
		print("\n")
		
		#####This is how you ensure the user is ready to continue with a key stroke
		try:
			input("Press any key to return to the main menu")
		except SyntaxError:
			pass
		break	
	
#Main Menu
ans=True
while ans:
	main_title()
	print("""
		1.SSH Tunneling (Upto 4 Machines)
		2.Windows Port Forwarding
		3.Exit/Quit
		""")
	ans=raw_input("Select an Option above: ")
	if ans=="1":
		print("""
		1. SSH Tunneling with Up to 4 Targets
		2. SSH to 2 Target machines with multiple ports open
		3. Reverse SSH from inside a network to your Ops Machine. 
		4. Return to Main Menu	
		""")	
		ssh=raw_input("Select an Option Above:")
		if ssh=="1":
			ssh_tunnel1()
			
		elif ssh=="2":
			ssh_tunnel1_Multiport()
			
		elif ssh=="3":
			ssh_reverse_tunnel()
		
		elif ssh=="4":
			break
			
		else:
			print("\n Not Valid Choice Try again")
	   
	elif ans=="2":
		windows_port_forward()
		

	elif ans=="3":
		exit()
		
