# Network Port Scanner

A simple TCP port scanner implemented in Python using sockets.

## Description
This project scans a given IP address over a specified range of ports
and identifies open ports using TCP connect scanning.

## Technologies Used
- Python
- Socket Programming
- TCP Networking

## How It Works
- Attempts a TCP connection to each port
- If the connection succeeds, the port is marked as OPEN
- Uses timeouts to handle filtered or closed ports

## Usage
```bash
python scanner.py

## Sample Output
Scanning 127.0.0.1 from port 20 to 1024

[OPEN] Port 135
[OPEN] Port 445

## What I Learned
- How TCP port scanning works using socket connections
- Difference between open, closed, and filtered ports
- How timeouts affect network scanning speed
- Structuring a Python project using functions

## Future Improvements
- Multithreaded scanning for better performance
- Service detection based on common ports
- Command-line arguments for target and port range

