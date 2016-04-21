#! /usr/bin/env python

from scapy.all import *

with open('inpartb.txt', 'r') as f:
	src = f.readline().strip()
	dst = f.readline().strip()
	srcport = int(f.readline().strip())
	dstport = int(f.readline().strip())
	payload = f.readline().strip()

packet = IP(src=src, dst=dst)/TCP(dport=dstport, sport=srcport)/Raw(load=payload)
packet.show()
answer = sr1(packet)

