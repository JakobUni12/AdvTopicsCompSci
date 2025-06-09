from scapy.all import sniff, hexdump, Raw

def print_payload(pkt):
    if pkt.haslayer(Raw):
        hexdump(pkt[Raw].load)

sniff(filter="tcp port 8883", prn=print_payload, count=10)
