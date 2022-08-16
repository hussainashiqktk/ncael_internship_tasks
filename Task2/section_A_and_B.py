from re import sub
import socket
import platform
import os
from yaml import parse

#(a) get the ip addresses of all the interfaces on this pc

hostname = socket.gethostname()
ip = socket.gethostbyname_ex(hostname)
print("+--------------------------------------+")
print("hostname............. ", ip[0])
print("ip interface 0....... ", ip[2][1])
print("ip interface 1....... ", ip[2][2])
print("ip interface 2....... ", ip[2][3])
print("+--------------------------------------+")

#(b) get the OS name

os_name = platform.system()
print("Operating System Name............. ", os_name)
print("+--------------------------------------+")

#(c) get OS registered user
import getpass
os_user = getpass.getuser()
print("Registered user on OS............. ", os_user)
print("+--------------------------------------+")

#(d) 
import subprocess
id = subprocess.check_output(["systeminfo"]).decode("utf-8").split("\n")
print(id[4])
print(id[10])

#(f) get System MAC Address
from getmac import get_mac_address as gma
mac_addr = gma()
print("MAC Address............................ ", mac_addr)
print("+--------------------------------------+")

#----------------------------------------------------------------------------section B------------------------------------------------------------#

import json

#(a) writes all the above info in json object
ipslist = [x for x in ip[2]]
systeminfo_jsonlist = {
    "IPs" : ipslist,
    "os_system_name" : os_name,
    "os_manufacturer": id[4],
    "os_install_date" : id[10],
    "os_user" : os_user,
    "mac" : mac_addr
}
#(b) dumps the above via json, indent is for prettily printing the json
systeminfoJSONpretty = json.dumps(systeminfo_jsonlist, indent=3)
systeminfoJSON = json.dumps(systeminfo_jsonlist)
print(systeminfoJSON)

#(c) Make directory named Task2
os.mkdir("Task2")
os.chdir("Task2")

#(c) write the json into file task2.txt
f = open("task1.txt", "w")
f.writelines(systeminfoJSONpretty)
f.close()

#(d) print the json to terminal

f = open("task1.txt", "r")
print(f.readlines())
f.close()
