from scapy.all import *
import random

target_ip = "127.0.0.1"

for i in range(200):
    packet = IP(dst=target_ip)/UDP(
        sport=random.randint(1024,65535),
        dport=random.randint(1,65535)
    )/Raw(b"UDP Test")

    send(packet, verbose=0)

print("UDP packets sent")
