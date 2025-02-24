#!/bin/bash  
# Block all non-VPN traffic  
iptables -P INPUT DROP  
iptables -P OUTPUT DROP  
iptables -A OUTPUT -o tun0 -j ACCEPT  
