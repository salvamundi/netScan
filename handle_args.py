import argparse


def handle_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--method", dest = "method", help = "Network layer to perform scan on, type -m/--method help for additional info")
    parser.add_argument("-t", "--target", dest = "target", help = "Target IP or IP range")
    options = parser.parse_args()

    if options.method is None:
        options.method = "ARP"

    if options.target is None:
        print("[!] No target specified")
        print("[*] Shutting down...")
        exit()


    return options  # returns "method": value & "target": value
