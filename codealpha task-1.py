from scapy.all import sniff

def analyze_packet(packet):
    print(f"\n[+] Packets: {packet.summary()}")

    if packet.haslayer("IP"):
        ip_layer = packet["IP"]
        print(f"From: {ip_layer.src}")
        print(f"To:   {ip_layer.dst}")
        print(f"Protocol: {ip_layer.proto}")
    
    if packet.haslayer("TCP"):
        tcp_layer = packet["TCP"]
    print(f" source Port: {tcp_layer.sport}")
    print(f" Dest port: {tcp_layer.dport}")

print("the analyze of an packets is processing:")
sniff(prn=analyze_packet, count=100)  
print("The Network sniffing was successfully completed")
