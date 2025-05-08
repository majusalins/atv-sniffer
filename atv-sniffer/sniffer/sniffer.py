from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime
import argparse

def packet_callback(packet):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    
    if IP in packet:
        ip = packet[IP]
        src_ip = ip.src
        dst_ip = ip.dst
        protocol = ip.proto
        
        # Pacotes TCP
        if TCP in packet and (protocol == 6 or args.http_only and packet[TCP].dport == 80):
            tcp = packet[TCP]
            print(f"\n[+] {timestamp} - TCP Packet:")
            print(f"    Source: {src_ip}:{tcp.sport}")
            print(f"    Destination: {dst_ip}:{tcp.dport}")
            
            if args.verbose and packet.haslayer('Raw'):
                payload = bytes(packet['Raw']).decode('utf-8', errors='ignore')
                if 'HTTP' in payload or 'POST' in payload or 'GET' in payload:
                    print("    HTTP Data:", payload[:200]) 
        
        # Pacotes UDP
        elif UDP in packet and protocol == 17:
            udp = packet[UDP]
            print(f"\n[+] {timestamp} - UDP Packet:")
            print(f"    Source: {src_ip}:{udp.sport}")
            print(f"    Destination: {dst_ip}:{udp.dport}")
            
            if args.verbose and packet.haslayer('Raw'):
                payload = bytes(packet['Raw']).decode('utf-8', errors='ignore')
                print("    Data:", payload[:200])

def main():
    global args
    parser = argparse.ArgumentParser(description="Simple Packet Sniffer")
    parser.add_argument("-i", "--interface", help="Network interface to sniff on", default=None)
    parser.add_argument("-v", "--verbose", help="Show packet payload", action="store_true")
    parser.add_argument("--http-only", help="Only show HTTP packets", action="store_true")
    args = parser.parse_args()

    print("""
    ##### Sniffer de pacotes #####
    ---------------------
    Capturando pacotes TCP/UDP...
    Aperte Ctrl+C para parar.
    """)

    filter_str = "tcp or udp"
    if args.http_only:
        filter_str = "tcp port 80"

    try:
        sniff(iface=args.interface, prn=packet_callback, filter=filter_str, store=0)
    except PermissionError:
        print("\nERROR: Necessários privilégios de root!")
        print("Comando: sudo python3 sniffer.py\n")
    except KeyboardInterrupt:
        print("\nAplicação finalizada pelo usuário.")

if __name__ == "__main__":
    main()