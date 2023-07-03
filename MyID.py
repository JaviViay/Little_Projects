import platform
import requests
import socket
import uuid
import wmi
 
color_reset = "\033[0m"

if platform.system() == "Windows":
    so_color = "\033[94m"
elif platform.system() == "Linux" or "Java":
    so_color = "\033[33m"
elif platform.system() == "Darwin":
    so_color = "\033[96m"
else:
    so_color = "\033[93m"
print("Operative System:", so_color, platform.system(), color_reset)
print("  Version:", platform.version())
print("Name:", platform.node())
print("Processor Architecture:", platform.machine())
print()

def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    if response.status_code == 200:
        public_ip = response.json()['ip']
        return public_ip
print("Public IP:", "\033[32m", get_public_ip(), color_reset)
print("Private IP:", "\033[32m", socket.gethostbyname(socket.gethostname()), color_reset)
print()

def Mac():
    mac = uuid.getnode()
    return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
print("MAC:", "\033[95m", Mac(), color_reset)
print()

print("Hardware:") #"\033[31m"
print("  Drives:")

conn = wmi.WMI()
for disk in conn.Win32_DiskDrive():
    print("    Model:","\033[31m",disk.Model,color_reset)
    print("    Size:","\033[31m",disk.Size,color_reset)
    print("    Serial Number:","\033[31m",disk.SerialNumber,color_reset)

for cpu in conn.Win32_Processor():
    print("  CPU:")
    print("    CPU Name:","\033[31m",cpu.Name,color_reset)
    print("    Manufacturer:","\033[31m",cpu.Manufacturer,color_reset)
    print("    Cores:","\033[31m",cpu.NumberOfCores,color_reset)
    print()
