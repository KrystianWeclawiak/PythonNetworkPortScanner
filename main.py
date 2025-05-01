from datetime import datetime
import socket
from scanner import scan_ports

# getting target ip
target_ip = input("Enter IP Address of Target Server: ")
target_ip = socket.gethostbyname(target_ip)

# getting port scanning range
port_range = input("Enter Port Range of Target Server (start_port end_port): ")
start_port, end_port = port_range.split(" ")
start_port = int(start_port)
end_port = int(end_port)

# start banner
print("-" * 50)
print("Starting Network Scanner")
print("Started: {}".format(datetime.now()))
print("-" * 50)

# call the scanning function from the scanner module
time_taken = scan_ports(start_port, end_port, target_ip)

# result
print("-" * 50)
print("Stopping Network Scanner - All Ports from {} to {} scanned".format(start_port, end_port))
print(f"Time taken: {time_taken} sec")
print("-" * 50)
