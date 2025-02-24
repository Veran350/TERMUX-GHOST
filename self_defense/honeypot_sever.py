from flask import Flask, request  
app = Flask(__name__)  

@app.route('/')  
def trap():  
    with open("honeypot.log", "a") as f:  
        f.write(f"Attacker IP: {request.remote_addr}\n")  
    return "404 - Nothing here"  

if __name__ == "__main__":  
    app.run(host='0.0.0.0', port=8080)  
