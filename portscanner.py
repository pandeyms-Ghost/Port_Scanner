import socket
from IPy import IP
def scan(target):
    converted_ip=ipaddr(target)
    print("\n" +"[-_-] Scanning Target " + str(target))
    for port in range(int(input("Enter Starting range of port no. :")),int(input("Enter Ending range of port no. :"))):
        port_scanner(converted_ip, port)
def ipaddr(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)
def get_banner(sock):
    return sock.recv(1024)

def port_scanner(ipaddress,port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print("[+] Port " + str(port) + " : "+ str(banner.decode().strip("\n")))
        except:
            print("[+] Port " + str(port) + " is open")
    except:
        pass
if __name__ == "__main__":
    targets = input("[+] Enter target/s to scan(split multiple target with ,): ")
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(" "))
    else:
        scan(targets)
