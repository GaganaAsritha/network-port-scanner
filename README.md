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
