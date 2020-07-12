import os
import sys

def reverse(localport,localip):
   os.system("ssh -R "+localport+":127.0.0.1:61234 root@"+localip)
   
def remcom(remoteip,command):
   os.system("ssh root@"+remoteip+" "+command)

def scp(remoteip,foldername):
   os.system("scp -r "+foldername+" root@"+remoteip+":/week-1/")

def sftp(remoteip):
   os.system("sftp root@"+remoteip)

def proxy(ip,port):
   print("Changing the bash_profile...")
   os.system("echo export HTTP_PROXY="+ip+":"+port+" >> ~/.bash_profile")   
   os.system("echo export HTTPS_PROXY="+ip+":"+port+" >> ~/.bash_profile")
   print("Run the following command: source ~/.bash_profile")

if __name__=="__main__":
   
   if len(sys.argv) < 2:
       print("Usage:")
       print("python3 script.py tasknum")
       print("Tasknum:\n1:For Reverse Tunneling\n2:For Remote Command Execution using ssh\n3:Run the copy command\n4:Establish sftp connection\n5:Set Proxy")
       print("Reverse Tunneling: python3 script.py 1 localport localip\n")
       print("Remote Command Execution: python3 script.py 2 remoteip command\n")
       print("Copy Command: python3 script.py 3 remoteip foldername\n")
       print("SFTP: python3 script.py 4 remoteip\n")
       print("Set Proxy: python3 script.py 5 ip port")
       sys.exit(0)
   if sys.argv[1] == '1':
       reverse(sys.argv[2],sys.argv[3])
   elif sys.argv[1] == '2':
       remcom(sys.argv[2],sys.argv[3])
   elif sys.argv[1] == '3':
       scp(sys.argv[2],sys.argv[3])
   elif sys.argv[1] == '4':
       sftp(sys.argv[2])
   elif sys.argv[1] == '5':
       proxy(sys.argv[2],sys.argv[3])                    
           

