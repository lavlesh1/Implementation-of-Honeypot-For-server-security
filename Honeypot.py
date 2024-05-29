
from socket import *
from art import *
from termcolor import colored ,cprint
import time
import yagmail

#@copyright -- Anmol Pandey

def main():
    ip_add=input("Enter Ip Address of server :")
    port = int(input("Port of server :"))
    print(colored(''' 

                         ██░ ██  ▒█████   ███▄    █ ▓█████▓██   ██▓ ██▓███   ▒█████  ▄▄▄█████▓
                        ▓██░ ██▒▒██▒  ██▒ ██ ▀█   █ ▓█   ▀ ▒██  ██▒▓██░  ██▒▒██▒  ██▒▓  ██▒ ▓▒
                        ▒██▀▀██░▒██░  ██▒▓██  ▀█ ██▒▒███    ▒██ ██░▓██░ ██▓▒▒██░  ██▒▒ ▓██░ ▒░
                        ░▓█ ░██ ▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄  ░ ▐██▓░▒██▄█▓▒ ▒▒██   ██░░ ▓██▓ ░ 
                        ░▓█▒░██▓░ ████▓▒░▒██░   ▓██░░▒████▒ ░ ██▒▓░▒██▒ ░  ░░ ████▓▒░  ▒██▒ ░ 
                         ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░  ██▒▒▒ ▒▓▒░ ░  ░░ ▒░▒░▒░   ▒ ░░   
                         ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░▓██ ░▒░ ░▒ ░       ░ ▒ ▒░     ░    
                         ░  ░░ ░░ ░ ░ ▒     ░   ░ ░    ░   ▒ ▒ ░░  ░░       ░ ░ ░ ▒    ░      
                         ░  ░  ░    ░ ░           ░    ░  ░░ ░                  ░ ░           
                                                           ░ ░                                

    ''','red'))
    time.sleep(1)
    print(colored("[+] Esatablishing the Connection ......",'red'))
    time.sleep(2)
    print(colored("[*] HoneyPot is established on Server  ",'red'),end="")
    print(colored(ip_add,'green'),end="")
    print(colored(" on Port ",'red'),end="")
    print(colored("80",'green'))
    time.sleep(1)
    print(colored("[+] Honeypot started .....",'red'),end="")
    cprint(".....",'red',attrs=['blink'])
    try:
        get_socket_con = socket(AF_INET,SOCK_STREAM)
        get_socket_con.bind((ip_add,port)) 
        get_socket_con.listen(10)
        v=1
        A=1
        while 1:
            client_con,client_addr = get_socket_con.accept()
            data  = client_con.recv(2048)
            client_con.send(b"<h1 style='text-align:center'> !!! Sample Web Server !!! </h1>")
            b=data.decode('utf-8')
            f=b.find('HTTP')
            s=b[5:f]
            if(s=='favicon.ico '):
                cprint("\t\t\t\t\t\t\t\t\t\tVisitors Visited =[{}]".format(v),'green')
                cprint("\t!!! Visitor Found !!!",'green',attrs=['blink'])
                print()
                print(colored("\t\tVisiter IP --> [{}]".format(client_addr[0]),'yellow'))
                print(colored("\t\tConnection Port --> [{}]".format(client_addr[1]),'yellow'))
                print()
                v=v+1
                user = 'abc@gmail.com' #gmail of sender
                app_password = 'amtmshdbazbwjytb' # a token for gmail
                to = 'demo@gmail.com' #gmail to receive message
                subject = 'Visitor Information !!!'
                content = ['Visitor Ip --> [{}]'.format(client_addr[0]),'Visitor Port -> [{}]'.format(client_addr[1]),data.decode('utf-8'),'Total Visitors Found -->[{}]'.format(v)]
                with yagmail.SMTP(user, app_password) as yag:
                    yag.send(to, subject, content)
            elif(len(s)==1):
                cprint("\t\t\t\t\t\t\t\t\t\tVisitors Visited =[{}]".format(v),'green')
                cprint("\t!!! Visitor Found !!!",'green',attrs=['blink'])
                print()
                print(colored("\t\tVisiter IP --> [{}]".format(client_addr[0]),'yellow'))
                print(colored("\t\tConnection Port --> [{}]".format(client_addr[1]),'yellow'))
                print()
                user = 'abc@gmail.com'  #gmail of sender
                app_password = 'amtmshdbazbwjytb' # a token for gmail
                to = 'demo@gmail.com' #gmail to receive message
                subject = 'Visitor Information !!!'
                content = ['Visitor Ip --> [{}]'.format(client_addr[0]),'Visitor Port -> [{}]'.format(client_addr[1]),data.decode('utf-8'),'Total Visitors Found -->[{}]'.format(v)]
                with yagmail.SMTP(user, app_password) as yag:
                    yag.send(to, subject, content)
            else:
                cprint("\t\t\t\t\t\t\t\t\t\tAttacker\'s Traced =[{}]".format(A),'green')
                cprint("\t!!! Attacker Found !!!",'red',attrs=['blink'])
                print()
                print(colored("\t\tAttacker\'s IP --> [{}]".format(client_addr[0]),'yellow'))
                print(colored("\t\tConnection Port --> [{}]".format(client_addr[1]),'yellow'))
                print()
                A=A+1
                user = 'abc@gmail.com' # gmail of sender
                app_password = 'amtmshdbazbwjytb' # a token for gmail
                to = 'demo@gmail.com' #gmail to receive message
                subject = 'Attacker Found !!!'
                content = ['Attacker\'s Ip --> [{}]'.format(client_addr[0]),'Attacker\'s Port -> [{}]'.format(client_addr[1]),data.decode('utf-8'),'Attacker\'s Traced -->[{}]'.format(A)]
                with yagmail.SMTP(user, app_password) as yag:
                    yag.send(to, subject, content)    
            print(colored(data.decode('utf-8'),'yellow'))
    except error as identifier:
        print(colored("[+] Unspecified error [{}]".format(identifier),'red'))
    except KeyboardInterrupt as ky:
        print(colored("\n[-] Honeypot Terminated !",'red'))
        get_socket_con.close()
    finally:
        get_socket_con.close()
    get_socket_con.close()
if __name__ == "__main__":
    main()

