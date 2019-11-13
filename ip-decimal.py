#!/usr/bin/env python3
# JMM (@hot_sauce)
# IP Address Conversion Application

import ipaddress

def prBrCyan(skk): print("\033[91m {}\033[00m" .format(skk))

print("\r")
ip = ipaddress.IPv4Address(input("Enter IP Address: "))
print("\r")

ipInt = int(ipaddress.IPv4Address(ip))

print("IP Integer: ")
prBrCyan(ipInt) 

#print(ipInt)
print("\r")
