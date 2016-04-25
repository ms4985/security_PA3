#! /usr/bin/env python

import sys
from scapy.all import *
import random, string

srcport = int(sys.argv[1])
dstport = int(sys.argv[2])

loop = '127.0.0.1'

i=0
while(i<20):
	pkt1 = IP(dst=loop)/TCP(dport=3000+i, sport=srcport)
	send(pkt1)
	i += 1

i=0
while(i<5):
	payload = ''.join(random.choice(string.lowercase) for i in range(10))
	pkt2 = IP(dst=loop)/TCP(dport=dstport, sport=srcport)/Raw(load=payload)
	send(pkt2)
	i += 1
