#Version 0.5.4

version = "0.5.4"

import os
#osx = raw_input()

#if osx == "Linux":
while True:
  print("What would you like to do?")

  type=raw_input("Enter type: ")

  if type == "-h":
    print"Linux Help"
    print ""
    print"------------------------------------------------------------------------------------------"
    print"Type 'root' to switch user to root (only required for OS_scan and intense_scan) NOTE: THIS WILL EXIT THE PROGRAM!"
    print"------------------------------------------------------------------------------------------"
    print"Type 'simple_scan' ip for a simple scan this will give  general scan of what ports are on the network."
    print "example: simple_scan 192.168.1.1"
    print"------------------------------------------------------------------------------------------"
    print""
    print"------------------------------------------------------------------------------------------"
    print"Type 'ping' to ping the target and make sure its up. "
    print "example: ping 192.168.1.1"
    print"------------------------------------------------------------------------------------------"
    print""
    print"------------------------------------------------------------------------------------------"
    print"If you dont already have nmap type 'get'"
    print"------------------------------------------------------------------------------------------"
    print""
    print"------------------------------------------------------------------------------------------"
    print"Type 'version' to get the current version of the program."
    print""
    print"------------------------------------------------------------------------------------------"
    print"Type 'intense_scan' REQUIRES ROOT! to do an intense scan on the target showing open ports, os, open and closed ports"
    print"example: intense_scan 192.168.1.1"
    print"------------------------------------------------------------------------------------------"
    print"Type 'OS_scan' REQUIRES ROOT! to just see what operating systems are running on the server"
    print"example: OS_scan 192.168.1.1"
    print"------------------------------------------------------------------------------------------"
    print"Type 'range_scan' to scan a range of IPs"
    print"example: range_scan 192.168.1.0/24 (0/24 is that range)"
    print"------------------------------------------------------------------------------------------"
    print"Type 'exit' to exit the program"
    print"------------------------------------------------------------------------------------------Win"
  elif type == 'get':
    os.system("sudo apt-get install nmap")
    os.system("clear")
    print"You have successfully installed Nmap!"
    print""
    print""
  elif type == 'version':
    print version
  elif type == 'root':
    print""
    print "This is going to exit the program! You have to then launch the program again!"
    print""
    os.system("su")

  elif type == 'exit':
    print "Bye"
    exit()

  else:
    print"What is the ip you would like to scan?"
    ip=raw_input("Enter IP to scan")

    if type == 'simple_scan':
      os.system("nmap %s" % ip)
    if type == 'ping':
      os.system('ping -c 5 %s' % ip)
    if type == 'intense_scan':
      os.system("nmap -sV -O -sT --open %s" % ip)
    if type == 'OS_scan':
      os.system("nmap -O %s" % ip)
    if type == 'range_scan':
      os.system("nmap %s" % ip)


    else:
      print"Thats not a valid command! use -h if you arent sure!"
      print""

