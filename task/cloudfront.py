import os
def color(c):
    os.system('tput setaf {}'.format(c))
def clear():
    os.system('clear')
def cloud_front_func(cf_arg,ip):
    while(1):
        clear()
        color(7)
        print('\n\t\t\t\tCloud Front Menu')
        print('\t\t\t==================================\n')
        color(3)
        cloudfrontmenu=['Create Distribution','List all Distributions','Create Invalidation','List all Invalidations']
        for i in range(len(cloudfrontmenu)):
            print('\t\t\tEnter {} : {}'.format(i+1,cloudfrontmenu[i]))
        color(6)
        print('\t\t\tEnter 0 : Go Back')
        color(1)
        print('\t\t\tEnter e : To Exit')
        color(5)
        choice=input('Enter your choice : ')
        color(7)
        if choice=='0':
            from aws import aws_func
            aws_func(cf_arg,ip)
        elif choice=='1':
            bucket_name=input('Enter the Name of Bucket : ')
            os.system('{} {} aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com'.format(bucket_name))
        elif choice=='2':
            os.system('{} {} aws cloudfront list-distributions'.format(cf_arg,ip))
        elif choice=='3':
            distribution_id=input('Enter the Distribution ID : ')
            path=input('Enter the path of the file under Cloud Front : ')
            os.system('{} {} aws cloudfront create-invalidation --distribution-id {} --paths {}'.format(cf_arg,ip,distribution_id,path))
        elif choice=='4':
            distribution_id=input('Enter the Distribution ID : ')
            os.system('{} {} aws cloudfront list-invalidations --distribution-id {}'.format(cf_arg,ip,distribution_id))
        elif choice=='e':
            color(7)
            clear()
            exit()
        else:
            print('Invalid Choice !')
        input('Press Enter to continue....')