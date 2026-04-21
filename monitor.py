from scapy.all import sniff
from collections import defaultdict
import time

packet_count = defaultdict(int)
start_time = time.time()

def detect(packet):
    global packet_count

    if packet.haslayer("IP"):
        src = packet["IP"].src
        packet_count[src] += 1

        if packet_count[src] > 50:
            print(f"[ALERT] Possible DDoS from {src}")

    if time.time() - start_time > 10:
        packet_count.clear()

print("[*] Monitoring network...")
sniff(prn=detect, store=0)
