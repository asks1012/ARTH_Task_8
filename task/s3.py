import os
def color(c):
    os.system('tput setaf {}'.format(c))
def clear():
    os.system('clear')
def s3_func(s3_arg,ip):
    while(1):
        clear()
        color(7)
        print('\n\t\t\t\t    S3 Menu')
        print('\t\t\t==================================\n')
        color(3)
        s3_menu=['Show all Buckets','Create a Bucket','Delete a Bucket','Upload a file to bucket','Copy file from one bucket to the other','Download a file from a bucket','Recursively copy files to S3 bucket','Download all files from a bucket recursively','Show files in a bucket','Delete a file in a bucket','Delete all files in a bucket']
        for i in range(len(s3_menu)):
            if i<9:
                print('\t\t\tEnter {}  : {}'.format(i+1,s3_menu[i]))
            else:
                print('\t\t\tEnter {} : {}'.format(i+1,s3_menu[i]))
        color(6)
        print('\t\t\tEnter 0  : Go Back')
        color(1)
        print('\t\t\tEnter e  : To Exit')
        color(5)
        choice=input('Enter your choice : ')
        color(7)
        if choice=='0':
            from aws import aws_func
            aws_func(s3_arg,ip)
        if choice=='1':
            os.system('{} {} aws s3 ls'.format(s3_arg,ip))
        elif choice=='2':
            bucket_name=input('Enter the Bucket Name to be Created : ')
            region=input('Enter the Region Name : ')
            os.system('{} {} aws s3 mb s3://{} --region {}'.format(s3_arg,ip,bucket_name,region))
        elif choice=='3':
            bucket_name=input('Enter the Bucket Name to be Deleted : ')
            os.system('{} {} aws s3 rb s3://{} --force'.format(s3_arg,ip,bucket_name))
        elif choice=='4':
            path=input('Enter the path of file starting from / : ')
            bucket_name=input('Enter the Bucket Name : ')
            os.system('{} {} aws s3 cp {} s3://{}'.format(s3_arg,ip,path,bucket_name))
        elif choice=='5':
            bucket1=input('Enter the Source Bucket name : ')
            file_name=input('Enter the file name : ')
            bucket2=input('Enter the Destination Bucket name : ')
            file_name2=input('Enter the new file name : ')
            os.system('{} {} aws s3 cp s3://{}/{} s3://{}/{}'.format(s3_arg,ip,bucket1,file_name,bucket2,file_name2))
        elif choice=='6':
            bucket_name=input('Enter the bucket name : ')
            file_name=input('Enter the name of the file in Bucket : ')
            file_name2=input('Enter the new file name : ')
            os.system('{} {} aws s3 cp s3://{}/{} {}'.format(s3_arg,ip,bucket_name,file_name,file_name2))
        elif choice=='7':
            path=input('Enter the path of Directory starting from / : ')
            bucket_name=input('Enter the Bucket Name : ')
            os.system('{} {} aws s3 cp {} s3://{}/ --recursive'.format(s3_arg,ip,path,bucket_name))
        elif choice=='8':
            bucket_name=input('Enter the Bucket Name : ')
            path=input('Enter the Destination Directory starting from / : ')
            os.system('{} {} aws s3 cp s3://{} {} --recursive'.format(s3_arg,ip,bucket_name,path))
        elif choice=='9':
            bucket_name=input('Enter the Bucket Name : ')
            os.system('{} {} aws s3 ls s3://{} --recursive --human-readable --summarize'.format(s3_arg,ip,bucket_name))
        elif choice=='10':
            bucket_name=input('Enter the Bucket Name : ')
            file_name=input('Enter the file name to be deleted : ')
            os.system('{} {} aws s3 rm s3://{}/{}'.format(s3_arg,ip,bucket_name,file_name))
        elif choice=='11':
            bucket_name=input('Enter the Bucket Name : ')
            os.system('{} {} aws s3 rm s3://{} --recursive'.format(s3_arg,ip,bucket_name))
        elif choice=='e':
            color(7)
            clear()
            exit()
        else:
            print('Invalid Choice !')
        input('Press Enter to continue....')