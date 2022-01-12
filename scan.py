import packet_crafter as pc
import scapy.all as scapy
import handle_args as ha


def scan(method, target):
    packet = pc.craft(method, target)
    answered = scapy.srp(packet, timeout = 1, verbose = 0)[0] # (<Results: TCP:0 UDP:0 ICMP:0 Other:1>, UN)

    hosts = []
    for element in answered:
        # element = 0(<Ether  dst=ff:ff:ff:ff:ff:ff type=ARP |<ARP  pdst=x.x.x.x |>>,
        # 1<Ether  dst=xx:xx:xx:xx:xx:xx src=xx:xx:xx:xx:xx:xx type=ARP |<ARP  hwtype=0x1 ptype=IPv4 hwlen=6 plen=4 op=is-at hwsrc=xx:xx:xx:xx:xx:xx psrc=x.x.x.x)

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
        print("---\t\t---")

    print("----------------------------------")