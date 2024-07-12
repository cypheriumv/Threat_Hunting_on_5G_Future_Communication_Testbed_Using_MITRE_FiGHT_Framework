from scapy.all import *
from scapy.layers.inet import IP
from scapy.layers.sctp import SCTP
from scapy.packet import Packet, bind_layers
from scapy.fields import ByteField, ShortField, XByteField, StrLenField
import struct




# Define NAS layer (simplified example)
class NAS(Packet):
   name = "NAS Registration Request"
   fields_desc = [
       # 5GS Mobility Management (0x7E)
       # Fixed
       XByteField("protocol_discriminator", 0x7E),


       # Plain NAS message, not security protected (0x00)
       # 0x00 means no security, plain NAS message
       # Value will change if there is security
       # As of now, Fixed
       ByteField("security_header_type", 0x00),


       # Registration Request (0x41)
       # Fixed
       ByteField("message_type", 0x41),




       # 5GS Registration Type #
       # Typically 0
       BitField("spare_half_octet", 0, 4),


       # Indicates initial registration (0x01)
       # This value changes depending on the type of registration
       # (e.g., mobility registration update, periodic registration update).
       # Fixed
       BitField("registration_type", 1, 4),


       # NAS Key Set Identifier #
       # TSC (typically 0 for native security context)
       BitField("ngksi_tsc", 0, 1),
       # Typically 0
       BitField("spare_half_octet2", 0, 3),
       # NAS key set identifier (0x07 for not available)
       # Fixed, value of 7 used to indicate no key set id avail
       BitField("nas_key_set_identifier", 7, 4),


       # Mobile Identity (variable values based on context) #
       # Length of the mobile identity
       # Will vary depending on the actual length of the mobile identity being used
       # Value is length of the mobile_identity_value field +
       # the length of the mobile_identity_type
       ByteField("mobile_identity_len", 0x10),
       # 0x01 (5G-S-TMSI)
       # Can be other types such as 0x02 (5G-GUTI), 0x03 (IMEI), etc.
       # The type used should reflect the actual mobile identity format.
       # Variable: Type of mobile identity
       ByteEnumField("mobile_identity_type", 0x02, {0x01: "5G-S-TMSI", 0x02: "5G-GUTI", 0x03: "IMEI"}),
       # Variable: Actual mobile identity value
       StrFixedLenField("mobile_identity_value", "999400000534973", length_from=lambda x: x.mobile_identity_len - 1),


   ]




# Define NGAP layer (simplified example)
class NGAP(Packet):
   name = "NGAP"
   fields_desc = [
       #Fixed
       ByteField("message_type", 0x01),
       # Fixed
       ShortField("procedure_code", 0x0001),
       # Varies based on criticality
       ByteField("criticality", 0x01),
       # Calculated dynamically
       ShortField("length", 0),  # Will be calculated dynamically


       # Used to carry the NAS message.
       StrLenField("nas_pdu", "", length_from=lambda pkt: pkt.length),
       # Add more fields as needed
   ]


   def post_build(self, p, pay):
       if self.length == 0:
           length = len(pay)
           p = p[:3] + struct.pack("!H", length) + p[5:]
       return p + pay




# Bind layers
# To bind the NAS layer to the NGAP layer
bind_layers(NGAP, NAS, message_type=0x01)


# NAS Registration Request inside an NGAP Initial UE Message
nas_packet = NAS()
nas_packet.show()
ngap_packet = NGAP(nas_pdu=bytes(nas_packet))


# Display the crafted packet
ngap_packet.show()


# Sending the packet to AMF
send(IP(dst="192.168.251.2")/SCTP()/ngap_packet)
