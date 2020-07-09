import paramiko

client = paramiko.SSHClient()

hostName = input("Host Name(IP Address of phone): ")
#hostName = '192.168.1.91'
#username = 'root'
#password = 'alpine'
#port = '22'

username = input("Username: ")
password = input("Password: ")
port = input("What is the port number? ")

save = input("Save this data? Type yes or no: ")

if save == yes:
    info = {"host": hostName, "user": username, "pass": password, "port", port}
    

client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostName, port, username, password)
stdin,stdout,stderr = client.exec_command('cd ~')
stdin,stdout,stderr = client.exec_command('ls')
print(stdout.readlines())

client.close()
