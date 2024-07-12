from scapy.all import *
from scapy.contrib.bgp import *

def create_bgp_update(dst_ip="192.168.254.1", dst_port=179, src_port=179, asn=65001, prefix="192.0.2.0/24"):
    # Construct the BGP header and UPDATE message
    bgp_header = BGPHeader(type=2)  # UPDATE message

    # For now, skip the AS_PATH attribute until we clarify its correct usage
    bgp_update = BGPUpdate()  # This will be a very basic UPDATE message

    # Create IP and TCP layers
    ip = IP(dst=dst_ip)
    tcp = TCP(sport=src_port, dport=dst_port)

    # Stack the layers and return the packet
    return ip/tcp/bgp_header/bgp_update

# Packet construction and send
bgp_update_packet = create_bgp_update()
send(bgp_update_packet)