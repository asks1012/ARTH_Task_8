import os
import getpass
from loc_rem import local_remote

def color(c):
    os.system('tput setaf {}'.format(c))
def clear():
    os.system('clear')
color(6)
clear()
password=getpass.getpass('Enter Password : ')
if(password!='a'):
    color(1)
    print('Incorrect Authentication')
    color(7)
    exit()

local_remote()