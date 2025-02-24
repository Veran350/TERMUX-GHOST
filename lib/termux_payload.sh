#!/bin/bash  
# Bypass Android restrictions  
termux-microphone-record -l && \  
termux-telephony-call --reset && \  
settings put global airplane_mode_on 0  
