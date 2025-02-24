from Crypto.Cipher import AES  

class GhostEncrypt:  
    def __init__(self):  
        self.key = b'VERAN666-MAFIA-BOSS'  # 16/24/32 bytes key  

    def encrypt(self, data):  
        cipher = AES.new(self.key, AES.MODE_EAX)  
        return cipher.encrypt(data)  
