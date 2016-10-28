#!/bin/sh

iptables="/sbin/iptables"

# Get Host IP and Netmasks
# We got two interfaces

HOST_IP0="`/sbin/ifconfig eth0 | grep 'inet addr' | awk '{print $2}' | sed -e 's/.*://'`"
HOST_IP1="`/sbin/ifconfig eth1 | grep 'inet addr' | awk '{print $2}' | sed -e 's/.*://'`"
LOCAL_NETWORK1="`/sbin/ifconfig eth1 | grep 'inet addr' | awk -F '[ .:]' '{print $13"."$14"."$15".0/24"}'`"
LOCAL_NETWORK2="`/sbin/ifconfig eth0 | grep 'inet addr' | awk -F '[ .:]' '{print $13"."$14"."$15".0/24"}'`"

################################################################################################################
# Define Some Variables
# 公司的出口ip
IP_Fixed1="180.166.202.100"
IP_Fixed2="58.246.176.100"

################################################################################################################
# 0. Flushing iptables
$iptables -F
$iptables -t nat -F
$iptables -Z INPUT
$iptables -P INPUT ACCEPT

################################################################################################################
# 1. DROP Invalid packet
$iptables -A INPUT -m state --state INVALID -j DROP
$iptables -A OUTPUT -m state --state INVALID -j DROP

################################################################################################################
# 2. Allow All Service From
# From Localhost
$iptables -A INPUT -s 127.0.0.1 -j ACCEPT
$iptables -A INPUT -s $HOST_IP0 -j ACCEPT
$iptables -A INPUT -s $HOST_IP1 -j ACCEPT

# From Control Server
$iptables -A INPUT -s $LOCAL_NETWORK1  -j ACCEPT
$iptables -A INPUT -s $LOCAL_NETWORK2  -j ACCEPT

#$iptables -A INPUT -s $VPN_Srv -j ACCEPT
$iptables -A INPUT -s $IP_Fixed1 -j ACCEPT
$iptables -A INPUT -s $IP_Fixed2 -j ACCEPT

################################################################################################################
# 3. Allow Local to external connections

# * TCP service
$iptables -A INPUT -p tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT
$iptables -A INPUT -p tcp --sport 80 -m state --state ESTABLISHED -j ACCEPT
$iptables -A INPUT -p tcp --sport 443 -m state --state ESTABLISHED -j ACCEPT

# * DNS Service
$iptables -A INPUT -p udp --sport 53 -j ACCEPT
$iptables -A INPUT -p tcp --sport 53 -j ACCEPT

# * Game Service
#$iptables -A INPUT -p udp -m multiport --sports 9000,9001 -j ACCEPT
#$iptables -A INPUT -p tcp -m multiport --sports 9000,9001 -j ACCEPT

################################################################################################################
# 4. Open ports
#$iptables -A INPUT -p tcp --dport 22 -m state --state NEW,ESTABLISHED -j ACCEPT
$iptables -A INPUT -p tcp --dport 80 -m state --state New,ESTABLISHED -j ACCEPT
#$iptables -A INPUT -p tcp --dport 3306 -s $shop -m state --state NEW,ESTABLISHED -j ACCEPT

#  Open Game Server
$iptables -A INPUT -p tcp -m multiport --dports 9101,9002 -m state --state NEW,ESTABLISHED -j ACCEPT

################################################################################################################
# 5. Config Deny Ruleset

# * Reject All Syn Packet
$iptables -A INPUT -p tcp --syn -j REJECT

# * Drop All TCP packet
$iptables -A INPUT -p tcp --dport 1:65535 -j DROP

# * Drop All UDP packet
$iptables -A INPUT -p udp --dport 1:65535 -j DROP

# * Drop ping request
$iptables -A INPUT -p icmp --icmp-type echo-request -j DROP

################################################################################################################
# 6. Runing Finished
echo
echo "$HOST_IP0 + $HOST_IP1 Runing Finished ! "
echo

