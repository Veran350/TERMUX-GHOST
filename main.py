from core.vpn_handler import GhostVPN  
from core.wifi_god import deauth_nuke  

if __name__ == "__main__":  
    vpn = GhostVPN()  
    vpn.start()  
    target = input("[+] Target WiFi ESSID: ")  
    deauth_nuke(target)  
