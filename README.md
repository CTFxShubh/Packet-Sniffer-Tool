# PRODIGY_CS_Task-05
Packet Sniffer Tool

#  Basic Network Sniffer 

This project is an advanced network sniffer built using Python and the `scapy` library. It captures, analyzes, and logs network traffic, offering insights into the flow of data within a network.

## Features

- **Protocol Filtering**: Captures only IP, TCP, UDP, and ICMP packets.
- **Packet Parsing**: Extracts and displays source and destination IP addresses, ports, and protocol type.
- **Live Summary**: Prints a real-time summary of captured packets to the console.
- **File Logging**: Logs captured packet details with timestamps to a file (`captured_packets.log`) for later analysis.

## Prerequisites

Before running the network sniffer, ensure you have the following installed:

- **Python 3.x**: The script is written in Python 3, so you'll need Python installed on your machine.
- **Scapy**: Scapy is a powerful Python library used for network packet manipulation. It can be installed via pip.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/CTFxShubh/PRODIGY_CS_Task-05.git
   cd PRODIGY_CS_Task-05
   ```

2. **Install Dependencies**:

   Install the required Python libraries using pip:

   ```bash
   pip install scapy
   ```

## Usage

 **Run the Sniffer**:

   The network sniffer needs to be run with administrator privileges because packet sniffing requires elevated permissions. Run the script using:

   ```bash
   sudo python3 networksniffer.py
   ```

## Demonstration

To provide a better understanding of how the Packet Sniffer Tool operates, we have included a video demonstration below. This demo showcases the tool's functionality, highlighting how it captures and analyzes network packets in real-time. Please refer to the video for a step-by-step walkthrough of the tool in action.

Watch the [video demo](https://www.youtube.com/watch?v=YOUR_VIDEO_ID_HERE) of the Packet Sniffer Tool in action.

## Logging

The `captured_packets.log` file stores the following details for each captured packet:

- **Timestamp**: The exact date and time the packet was captured.
- **Protocol**: The protocol type (TCP, UDP, ICMP).
- **Source**: The source IP address and port number.
- **Destination**: The destination IP address and port number.

This log file is useful for reviewing the captured packets at a later time, making it suitable for network monitoring and forensic analysis.

## Further Enhancements

This basic network sniffer can be expanded with additional features:

- **PCAP File Saving**: Save captured packets to a `.pcap` file for in-depth analysis using tools like Wireshark.
- **Email Alerts**: Automatically send alerts via email when specific types of packets are detected.
- **GUI Integration**: Develop a graphical user interface to visualize network traffic in real-time and provide user-friendly controls.
