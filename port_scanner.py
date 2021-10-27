import socket
from common_ports import ports_and_services

def get_open_ports(target: str, port_range: list, verb=False):
    
    # Validating the given target
    try:
        ip_addr = socket.gethostbyaddr(target)
    except socket.gaierror:
        if target[0].isalpha():
            return "Error: Invalid IP address"
        else:
            return "Error: Invalid hostname"
    
    open_ports = []
    
    # Searching for open ports
    for port in range(port_range[0], port_range[1]):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Ipv4
        if s.connect_ex((ip_addr, port)) == 0:
            open_ports.append(port)
        s.close    
    
    if verb == True:
        ports = ""
        if len(ip_addr) > 0:
            ports = f"Open ports for {socket.gethostbyname(target)} ({ip_addr})\n"
        ports += "PORT    SERVICE"
        for p in open_ports:
            str_ports = str(p)
            while len(str_ports) < 4:
                str_ports += " "
            str_ports += "\n" + str_ports + "    " + ports_and_services[int(str_ports)]  
    else:
        return open_ports        
            
get_open_ports("209.216.230.240", [440, 445])