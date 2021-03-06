import os
def color(c):
    os.system('tput setaf {}'.format(c))
def clear():
    os.system('clear')
def aws_func(aws_arg,ip):
    while(1):
        clear()
        color(7)
        print('\t\t\t      AWS Menu')
        print('\t\t==================================\n')
        color(3)
        aws_menu=['Configure','EC2','S3','Cloud Front']
        for i in range(len(aws_menu)):
            print('\t\t\tEnter {} : {}'.format(i+1,aws_menu[i]))
        color(6)
        print('\t\t\tEnter 0 : Go Back')
        color(1)
        print('\t\t\tEnter e : To Exit')
        color(5)
        choice=input('Enter your choice : ')
        color(7)
        if choice=='0':
            from main_menu import main_men
            main_men(aws_arg,ip)
        elif choice=='1':
            os.system('{} {} aws configure'.format(aws_arg,ip))    
        elif choice=='2':
            from ec2 import ec2_func
            ec2_func(aws_arg,ip)
        elif choice=='3':
            from s3 import s3_func
            s3_func(aws_arg,ip)
        elif choice=='4':
            from cloudfront import cloud_front_func
            cloud_front_func(aws_arg,ip)
        elif choice=='e':
            clear()
            color(7)
            exit()
        else:
            print('Invalid Choice !')
        input('Press Enter to Continue....')