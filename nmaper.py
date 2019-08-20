import os
import sys
from os import system
from time import sleep

system('resize -s 32 94')

#check's if the system is root
def check_root():
    system('clear')
    if os.geteuid() != 0:
        print(banner)
        print('\n\033[1m\033[93m ✔ You need root privileges to run this script.\n')
        exit("\n ✔ Please try again, using 'sudo'\n\033[0m")
    else:
        pass

#have to add a function to check if nmap is installed
#def check_nmap():

retu = '\n\033[93m\033[1m◉ press ( y ) if you want to return to the main menu: \033[0m'

comp = '\n\033[31m\033[1m[✔] Scan Complete...\033[0m'

banner = '''\n\033[31m\033[1m
         	    _  _____ _   _    _    _   _    _    ____ ___ _   _ ____ 
         	   / \|_   _| | | |  / \  | \ | |  / \  / ___|_ _| | | / ___| 
         	  / _ \ | | | |_| | / _ \ |  \| | / _ \ \___ \| || | | \___ \ 
         	 / ___ \| | |  _  |/ ___ \| |\  |/ ___ \ ___) | || |_| |___) | 
        	/_/   \_\_| |_| |_/_/   \_\_| \_/_/   \_\____/___|\___/|____/


                            	   Coded By : Shyam Acharjya
                               	      Codename : P@seid0n
                       	      contact : pythonmonkey@tutanota.com\033[0m\n\n'''

def ret():
    sleep(0.5)
    print(comp)
    sleep(0.5)
    re0 = input(retu)
    if re0 == 'y' or re0 == 'yes':
        return menu()
    else:
        pass

def choice():
        csrf = input('\n [✔] Enter the target: ')
        system('clear')

def menu():
    system("clear")
    print(banner)
    print("\033[93m\033[1m ◉ ◉ Nmap Basic scans: \033[0m")
    print('''\033[1m 
 [0] Ping Scan								[1] Quick Scan
 [2] Quick Traceroute							[3] Quick Scan Plus
 [4] Intense Scan TCP							[5] Intense Scan UDP''')
    print("\n\033[93m\033[1m ◉ ◉ Nmap Best Scripts: \033[0m")
    print('''\033[1m
 [6] Cross Site Request Forgery						[7] Smb_ms17_o10
 [8] Dns Brutforce							[9] Firewall Bypass
 [10] Smb_ms08_067							[11] Smb_ms07_029
 [12] Rdp_ms12_020							[13] Ssl-heartbleed
 [14] Mysql dump hashes							[15] Smtp-enum-users\n''')
    choice = input("\033[93m root@noob: ")
    #setup for nmap scans
    if choice == '0':
        ping = input('\n [✔] Enter the target: ')
        system('nmap -sn ' + ping)
        ret()
    elif choice == '1':
        quickinput = input('\n [✔] Enter the target: ')
        system('nmap -T4 -F ' + quickinput)
        ret()
    elif choice == '2':
        troute = input('\n [✔] Enter the target: ')
        system('nmap -sn --traceroute ' + troute)
        ret()
    elif choice == '3':
        qsp = input('\n [✔] Enter the target: ')
        system('nmap -sV -T4 -O -F --version-light ' + qsp)
        ret()
    elif choice == '4':
        intcp = input('\n [✔] Enter the target: ')
        system('nmap -p 1-65535 -T4 -A -v ' + intcp)
        ret()
    elif choice == '5':
        inudp = input('\n [✔] Enter the target: ')
        system('nmap -sS -sU -T4 -A -v ' + inudp)
        ret()

	#have to add nmap script scans

    elif choice == '6':
        choice()
        system('nmap ' + csrf)
        ret()
    elif choice == '7':
        choice()
        system('nmap ' + csrf)

	#handle any unexpected inputs
    else:
        print('\n [*] select from any of the given options...')
        sleep(2)
        return menu()

if __name__ == '__main__':
    try:
        check_root()
        menu()
    except KeyboardInterrupt:
        print("\n\n [✘] Keyboard Interrupted [✘] \n")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
