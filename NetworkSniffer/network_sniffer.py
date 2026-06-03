from scapy.all import sniff, IP

def packet_callback(packet):
    if packet.haslayer(IP):
        src = packet[IP].src
        dst = packet[IP].dst
        proto = packet[IP].proto

        print(f"Source IP: {src}")
        print(f"Destination IP: {dst}")
        print(f"Protocol: {proto}")
        print("-" * 40)

sniff(prn=packet_callback, store=False, count=1)