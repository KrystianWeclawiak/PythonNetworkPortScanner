# PythonNetworkPortScanner

A simple Python-based network port scanner project that's a part of my Blue Team "Introduction To Python" Certificate. It checks the open port on a remote server within a specified range. It can be used to check the availability of certain services on a server.

### Features 
- detect open port on the server
- multithreaded scanning for faster results
- configurable port timeout
- scan a specified range of ports on a target server

### Requirements
- python 3.7 or later
- OS: Linux, Windows, macOS
- no external dependencies - uses only Python built-in libraries:
    - socket
    - datetime
    - time
    - threading

### Optional
If you plan to extend this project, you may need additional libraries such as argparse for command-line argument parsing 

## Installation
1. Clone the repository to your local machine.
```bash
git clone https://github.com/KrystianWeclawiak/PythonNetworkPortScanner.git
```

## Configuration
- Port Timeout:
    - You can modify the port scanning timeout by changing the `port_scanning_timeout` variable in the `scanner.py` module. The default is 3 second
- Port range:
    - The default scanning behaviour allows the user to enter a port range when prompted. Modify the input to change the range you want to scan

## Usage
1. Navigate to the project directory
```bash
cd PythonNetworkPortScanner
```
2. Run the main.py file
```bash
python main.py
```
3. You will be prompted to enter the IP address of the target server and the port range you want to scan
- Example input:
    ```bash
    Enter IP Address of Target Server: 127.0.0.1
    Enter Port Range of Target Server (start_port end_port): 1 1024
    ```
4. The program will output open ports on the target server within the specified range and provide the info how long scanning took
- Example output
    ```bash
    --------------------------------------------------
    Starting Network Scanner
    Started: 2025-05-01 12:21:23.095640
    --------------------------------------------------
    Port 22 is open
    Port 80 is open
    Port 443 is open
    --------------------------------------------------
    Stopping Network Scanner - All Ports from 1 to 1024 scanned
    Time taken: 1.325 sec
    --------------------------------------------------
    ```

## Contributing
Feel free to open issues or contribute to the project by forking the repository and submitting pull requests


