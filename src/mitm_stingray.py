import logging
from scapy.all import *

class MITMStingray:
    def __init__(self, interface):
        self.interface = interface
        self.devices = {}

    def start(self):
        logging.info("Starting MITM Stingray module...")
        sniff(iface=self.interface, prn=self.packet_handler, store=0)

    def packet_handler(self, packet):
        if packet.haslayer(Dot11):
            mac_address = packet.addr2
            if mac_address not in self.devices:
                self.devices[mac_address] = {
                    "SSID": packet.info.decode() if packet.info else "Unknown",
                    "Signal": packet.dBm_AntSignal if hasattr(packet, "dBm_AntSignal") else "Unknown"
                }
                logging.info(f"New device detected: {mac_address} - SSID: {self.devices[mac_address]['SSID']} - Signal: {self.devices[mac_address]['Signal']}")

    def render(self):
        return "MITM Stingray Module: Ready to intercept mobile device communications and collect sensitive data."
