import os
def color(c):
    os.system('tput setaf {}'.format(c))
def clear():
    os.system('clear')

# Resize LV
def resizeLV():
	os.system("clear")
	print()
	print("\nResize the Size of Logical Volume")
	print("\n----------------------------------------")
	print()

	size = input("\nEnter the Size : ")

	os.system("lvextend --size +{} /dev/{}/{}".format(size, vgName, lvName))
	os.system("resize2fs /dev/{}/{}".format(vgName, lvName))
	os.system("df -h")

	input("\nPress Enter to Continue")


# Create LVM
def createLVM():
	global vgName
	global lvName

	os.system("clear")
	print()
	print("\nCreate and Mount Logical Volume")
	print("\n--------------------------------------")
	print()

	disk = input("\nEnter the disk Name : ")
	os.system("pvcreate {}".format(disk))
	os.system("pvdisplay {}".format(disk))
	vgName = input("\nEnter the Virtual Group Name : ")
	os.system("vgcreate {0} {1}".format(vgName, disk))
	os.system("vgdisplay {0}".format(vgName))
	lvName = input("Enter the Locial Volume Name : ")
	lvSize = input("Enter the size of partation : ")
	os.system("lvcreate --size {} --name {} {}".format(lvSize, lvName,  vgName))
	os.system("lvdisplay {}/{}".format( vgName,  lvName))
	fs = input("\nEnter the File System : ")
	os.system("mkfs.{} /dev/{}/{}".format(fs, vgName, lvName))
	mount_point = input("\nEnter the Mountpoint : ")
	os.system("mount /dev/{0}/{1} {2}".format(vgName, lvName, mount_point))
	os.system("df -h")

	input("\nPress Enter to Continue")



# Create partition in local system
def createPartition():
	global vgName
	global lvName

	os.system("clear")
	print()
	print("Create and Mount Partition\n")
	print("--------------------------------------\n")
	print()

	disk = input("\nEnter the Disk Name : ")
	os.system("fdisk {}".format(disk))
	fs = input("\n Enter the File System : ")
	partitionName = input("\nEnter the Partition Name : ")
	os.system("mkfs.{} {}".format(fs, partitionName))
	mountPoint = input("\nEnter the Mountpoint : ")
	os.system("mount {} {}".format(partitionName, mountPoint))
	os.system("df -h")

	input("\n Press Enter to Continue")



# List disk available on Local system
def ListDisk():
	os.system("clear")
	print()
	print(" Check Disk is Available or Not")
	print("----------------------------------------")
	print()

	os.system("fdisk -l")
	print("Press Y to continue if disk is available.\n")
	print("Press N to exit the program if disk is not available. \n")
	ch = input("Enter your choice(Y/N): " )
	if ch == "N":
		os.system("clear")
		print()
		print("Add the Disk First")
		print("Thank You for using Partation Manager")
		exit()


# Linux Local Login
def linux_func(lin_arg,ip):
    while True:
        clear()
        color(7)
        print('\t\t\t        Linux Menu')
        print('\t\t    ==================================\n')
        color(3)
        print("""
                        Press 1 : Check IP Address
                        Press 2 : Run Command
                        Press 3 : Deploy Webserver
                        Press 4 : Create Partition
                        Press 5 : Create LVM
                        Press 6 : Resize LV
        """)

        color(6)
        print('\t\t\tEnter 0 : Go Back')
        color(1)
        print('\t\t\tEnter e : To Exit')
        color(5)
        choice=input('Enter your choice : ')
        color(7)

        if choice=='0':
            from main_menu import main_men
            main_men(lin_arg,ip)

        if choice == '1':
            os.system("ifconfig enp0s3")
            input()

        elif choice == '2':
            cmd = input("Enter the Command : ")
            os.system(cmd)
            input()


        elif choice == '3':
            os.system('yum install httpd -y')
            os.system('cp index.html /var/www/html/index.html')
            os.system('systemctl start httpd')
            os.system('systemctl status httpd')
            input()	

        elif choice == '4':
            ListDisk()
            createPartition()

        elif choice == '5':
            ListDisk()
            createLVM()

        elif choice == '6':
            resizeLV()

        elif choice=='e':
            clear()
            color(7)
            exit()
        else:
            print('Invalid Choice !')
        input('Press Enter to Continue....')