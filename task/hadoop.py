import os
def color(c):
    os.system('tput setaf {}'.format(c))
def clear():
    os.system('clear')
def hadoop_func(had_arg,ip):
    while(1):
        clear()
        color(7)
        print('\n\t\t\t\t     Hadoop Menu')
        print('\t\t\t==================================\n')
        color(6)
        hadoop_menu=['Download and Install JDK','Download and Install Hadoop','Configure Name Node','Configure Data Node','See version of Hadoop','Show the cluster report','Show all files in the cluster','Upload a file to cluster','Remove a file from cluster','Read a file from cluster','Upload a file with specific block size','Make a directory in Cluster','Know the status of safemode','Leave the safe mode']
        for i in range(len(hadoop_menu)):
            if i<9:
                print('\t\t\tEnter {}  : {}'.format(i+1,hadoop_menu[i]))
            else:
                print('\t\t\tEnter {} : {}'.format(i+1,hadoop_menu[i]))
        color(45)
        print('\t\t\tEnter 0  : Go Back')
        color(1)
        print('\t\t\tEnter e  : To Exit')
        color(5)
        choice=input('Enter your choice : ')
        color(7)
        if choice=='0':
            from main_menu import main_men
            main_men(had_arg,ip)
        elif choice=='1':
            os.system('{} {} wget 35.244.242.82/yum/java/el7/x86_64/jdk-8u171-linux-x64.rpm'.format(had_arg,ip))
            os.system("{} {} rpm -ivh jdk-8u171-linux-x64.rpm".format(had_arg,ip))
        elif choice=='2':
            os.system("{} {} wget https://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm".format(had_arg,ip))
            os.system("{} {} rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force".format(had_arg,ip))
        elif choice=='3':
            text='\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/name_node</value>\n</property>\n</configuration>\n'
            os.system('mkdir /name_node')
            os.system('echo "{}" >>/etc/hadoop/hdfs-site.xml'.format(text))
            master_ip=input('Enter the IP of master node : ')
            os.system('echo "\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n</configuration>\n">>/etc/hadoop/core-site.xml'.format(master_ip))
            os.system('hadoop-daemon.sh start namenode')
        elif choice=='4':
            text='\n<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/data_node</value>\n</property>\n</configuration>\n'
            os.system('mkdir /data_node')
            os.system('echo "{}" >>/etc/hadoop/hdfs-site.xml'.format(text))
            master_ip=input('Enter the Master IP : ')
            os.system('echo "\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n</configuration>\n" >>/etc/hadoop/core-site.xml'.format(master_ip))
            os.system('hadoop-daemon.sh start datanode')
        elif choice=='5':
            os.system('hadoop version')
        elif choice=='6':
            os.system('hadoop dfsadmin -report')
        elif choice=='7':
            os.system('hadoop fs -ls /')
        elif choice=='8':
            path=input('Enter the path of the file : ')
            os.system('hadoop fs -put {} /'.format(path))
        elif choice=='9':
            path=input('Enter the path of the file in cluster : ')
            os.system('hadoop fs -rm {}'.format(path))
        elif choice=='10':
            path=input('Enter the path of the file in cluster : ')
            os.system('hadoop fs -cat {}'.format(path))
        elif choice=='11':
            path=input('Enter the path of the file to be uploaded : ')
            block_size=int(input('Enter the block size : '))
            os.system('hadoop fs -Ddfs.block.size={} -put {} /'.format(block_size,path))
        elif choice=='12':
            folder_name=input('Enter the directory name : ')
            os.system('hadoop fs mkdir /{}'.format(folder_name))
        elif choice=='13':
            os.system('hadoop dfsadmin -safemode get')
        elif choice=='14':
            os.system('hadoop dfsadmin -safemode leave')
        elif choice=='e':
            clear()
            color(7)
            exit()
        else:
            print('Invalid Choice !')
        input('Press Enter to Continue....')