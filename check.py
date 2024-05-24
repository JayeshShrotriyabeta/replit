import socket

# Define a function to check if a port is open
def check_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)  # Timeout after 1 second
    try:
        s.connect((host, port))
        s.close()
        return True
    except (socket.timeout, socket.error):
        return False

# Define a list of common ports to check, including port 12345
common_ports = {
    "HTTP": 80,
    "HTTPS": 443,
    "SSH": 22,
    "FTP": 21,
    "SMTP": 25,
    "DNS": 53,
    "MySQL": 3306,
    "PostgreSQL": 5432,
    "MongoDB": 27017,
    "Redis": 6379,
    "CustomPort": 12345
}

# Define the host (usually 'localhost' or an IP address)
host = 'localhost'

# Check each port and print the result
for service, port in common_ports.items():
    if check_port(host, port):
        print(f"{service} ({port}) is open")
    else:
        print(f"{service} ({port}) is closed")
