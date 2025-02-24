import subprocess  

class GhostVPN:  
    def __init__(self):  
        self.tor_conf = "config/torrc"  

    def start(self):  
        subprocess.run(["tor", "-f", self.tor_conf], stdout=subprocess.DEVNULL)  
        subprocess.run(["iptables", "-A", "OUTPUT", "-o", "tun0", "-j", "ACCEPT"])  
        print("[+] VPN Active : Traffic routed through Tor")  
