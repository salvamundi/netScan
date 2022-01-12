import scapy.all as scapy


def craft(method, target):
    packet = None

    if method == "ARP":
        request = scapy.ARP(pdst = target)  # x.x.x.x
        broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")  # send to broadcast in order to send packet to each client
        packet = broadcast/request

    elif method == "ICMP":
        print("[!] Not supported yet")
        print("[*] Shutting down...")
        exit()
        ip = scapy.IP(dst = target)
        icmp = scapy.ICMP()
        packet = ip/icmp

    elif method == "TCP":
        print("[!] Not supported yet")
        print("[*] Shutting down...")
        exit()
        ip = scapy.IP(dst = target)
        tcp = scapy.TCP()
        packet = ip/tcp

    elif method == "UDP":
        print("[!] Not supported yet")
        print("[*] Shutting down...")
        exit()
        ip = scapy.IP(dst = target)
        udp = scapy.UDP()
        packet = ip/udp

    else:
        print("[!] Given method not available (try -h for help)")
        print("[*] Shutting down...")
        exit()

    return packet
