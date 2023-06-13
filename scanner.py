import socket
import sys
from datetime import datetime


if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguments")
    sys.exit()

print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(1, 1000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target, port))
        if result == 0:
            service = socket.getservbyport(port)
            print("Port {} ({}) is open".format(port, service))
        s.close()

except KeyboardInterrupt:
    print("\nExiting Program!!!")
    sys.exit()
except socket.gaierror:
    print("\nHostname could not be resolved!!!")
    sys.exit()
except socket.error:
    print("\nServer not responding!!!")
    sys.exit()
