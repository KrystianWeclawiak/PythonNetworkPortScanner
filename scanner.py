import socket
import threading
import time

# set the timeout duration
port_scanning_timeout = 3

# connect to a target port
def connect_to_target_port(port_number: int, target_ip_address: str):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(port_scanning_timeout)
        result = sock.connect_ex((target_ip_address, port_number))
        if result == 0:
            print(f"Port {port_number} is open\n")
        sock.close()
    except KeyboardInterrupt:
        print("\nExiting program.")
    except socket.gaierror:
        print("Hostname could not be resolved.")
    except socket.error:
        print("Could not connect to server.")

# start scanning ports
def scan_ports(start_port: int, end_port: int, target_ip: str):
    threads = []
    start_time = time.time()

    for port in range(start_port, end_port):
        thread = threading.Thread(target=connect_to_target_port, args=(port, target_ip))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    return end_time - start_time
