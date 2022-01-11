import scapy.all as scapy
import handle_args as ha

def scan(method, target):

    if method == "ARP":
        request = scapy.ARP(pdst = target)  # x.x.x.x
        broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")  # send to broadcast in order to send packet to each client
        packet = broadcast/request

    answered = scapy.srp(packet, timeout = 1, verbose = 0)[0]

    hosts = []
    for element in answered:
        p_src = element[1].psrc    # 192.168.0.102
        hw_src = element[1].hwsrc  # 00:11:22:33:44:55

        host = {"ip": p_src, "mac": hw_src}
        hosts.append(host)

    return hosts  # 'ip': <ip>, 'mac':<mac>


def show_hosts():
    options = ha.handle_args()  # values from -m & -t arguments
    hosts = scan(options.method, options.target)

    print("IP\t\tMAC")
    print("----------------------------------")
    print("---")

    for host in hosts:
        print(f"{host['ip']}\t{host['mac']}")
        print("---")

    print("----------------------------------")