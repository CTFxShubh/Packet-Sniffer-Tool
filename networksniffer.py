# Basic Network Sniffer Tool
# Written by: Shubh Patel
# Cyber Security Intern at Prodigy Infotech
# PRODIGY_CS_Task-05

from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime
import logging

# Configure logging to capture packets in a log file
logging.basicConfig(filename="captured_packets.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Callback function to process each captured packet
def packet_callback(packet):
    protocol = None
    src_port = None
    dst_port = None

    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst

        if TCP in packet:
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif UDP in packet:
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
        elif ICMP in packet:
            protocol = "ICMP"

        log_msg = f"Protocol: {protocol} | Source: {ip_src}:{src_port} -> Destination: {ip_dst}:{dst_port}"
        print(log_msg)
        logging.info(log_msg)

# Defining the packet filter 
packet_filter = "ip or tcp or udp or icmp"

# Start packet sniffing
sniff(filter=packet_filter, prn=packet_callback, store=0)

# End of Code  
