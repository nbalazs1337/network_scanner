#!/urs/bin/env python

import scapy.all as scapy

def scan(ip):
    #creating an ARP packet
    arp_request = scapy.ARP(pdst=ip)
    #for testing purpose, we can make use of the command
    #print(arp_request.summary())
    # listing all the fields for ARP function
    #scapy.ls(scapy.ARP())
    #we are creating an ethernet frame, and ethernet object from a class implemented by scapy
    broadcast = scapy.Ether()
    #creating a new packet which is the combination of the other two packets
    #we use forward slash becouse ware allowed by the scapy library
    arp_request_broadcast = broadcast/arp_request
    print(arp_request_broadcast.summary())
    # for showing more details about the contents of the packet
    arp_request_broadcast.show()




scan("10.0.2.1/24")