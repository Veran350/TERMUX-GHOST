import subprocess  

def rotate_mac():  
    subprocess.run("ip link set wlan0 down", shell=True)  
    subprocess.run("macchanger -r wlan0", shell=True)  
    subprocess.run("ip link set wlan0 up", shell=True)  
