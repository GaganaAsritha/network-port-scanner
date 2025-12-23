import socket
import time


#----------------------CONFIG----------------
target_ip="127.0.0.1"
start_port=20
end_port=1024
timeout=0.5
#--------------------------------------------

def scan_port(target_ip,port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(timeout)

    result=s.connect_ex((target_ip,port))
    s.close()

    return result==0


def scan_range(target_ip,start_port,end_port):
    print(f"Scanning {target_ip} from port {start_port} to {end_port}")

    start_time=time.time()

    for port in range(start_port,end_port+1):
        if scan_port(target_ip,port):
            print(f"[OPEN] Port {port}")

    end_time=time.time()
    duration=end_time-start_time

    print(f"\nScan completed in {duration:.2f} seconds")

if __name__ == "__main__":
    scan_range(target_ip,start_port,end_port)