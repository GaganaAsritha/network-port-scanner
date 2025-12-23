import socket

def scan_port(target_ip,port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.5)

    result=s.connect_ex((target_ip,port))
    s.close()

    return result==0


def scan_range(target_ip,start_port,end_port):
    print(f"Scanning {target_ip} from port {start_port} to {end_port}")

    for port in range(start_port,end_port+1):
        if scan_port(target_ip,port):
            print(f"[OPEN] Port {port}")


if __name__ == "__main__":
    target_ip="127.0.0.1"
    start_port=20
    end_port=1024

    scan_range(target_ip,start_port,end_port)