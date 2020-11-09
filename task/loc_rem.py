import os

def color(c):
    os.system('tput setaf {}'.format(c))
def clear():
    os.system('clear')

def local_remote():
    from main_menu import main_men
    clear()
    color(5)
    print('Where do you want to run the commands ?')
    color(2)
    print('''Enter 1 : local\nEnter 2 : remote''')
    color(5)
    print('Enter your choice : ',end='')
    location=input()
    if location=='2':
        clear()
        color(6)
        usr=input('Enter remote username : ')
        ip=input('Enter the remote IP   : ')
        os.system('tput setaf 3')
        print('Generating ssh key....\n')
        print('NOTE : If you don\'t know about ssh-keygen, Press Enter until you reach the step: "{}@{}\'s password"\n'.format(usr,ip))
        print('Under "{}@{}\'s password", type the password of the username: "{}"\n'.format(usr,ip,usr))
        os.system('tput setaf 7')
        os.system('ssh-keygen')
        os.system('ssh-copy-id {}@{}'.format(usr,ip))
        os.system('clear')
        main_men('ssh',ip)
    elif location=='1':
        main_men('','')
    else:
        color(1)
        print('Option not supported')
        os.system('sleep 2')
        local_remote()