import socket

# A dictionary of common ports and their descriptions
PORT_DESCRIPTIONS = {
 0:  {"tcp": True,  "udp": True,  "description": "Reserved"},
    1:  {"tcp": True,  "udp": True,  "description": "TCPMUX (TCP Port Service Multiplexer)"},
    5:  {"tcp": True,  "udp": True,  "description": "RJE (Remote Job Entry)"},
    7:  {"tcp": True,  "udp": True,  "description": "Echo Protocol"},
    9:  {"tcp": True,  "udp": True,  "description": "Discard Protocol"},
    11: {"tcp": True,  "udp": True,  "description": "Systat (Active Users)"},
    13: {"tcp": True,  "udp": True,  "description": "Daytime Protocol"},
    17: {"tcp": True,  "udp": True,  "description": "QOTD (Quote of the Day)"},
    19: {"tcp": True,  "udp": True,  "description": "CHARGEN (Character Generator)"},
    20: {"tcp": True,  "udp": False, "description": "FTP Data Transfer"},
    21: {"tcp": True,  "udp": False, "description": "FTP Command Control"},
    22: {"tcp": True,  "udp": True,  "description": "SSH (Secure Shell)"},
    23: {"tcp": True,  "udp": True,  "description": "Telnet (Unencrypted Remote Login)"},
    25: {"tcp": True,  "udp": True,  "description": "SMTP (Simple Mail Transfer Protocol)"},
    37: {"tcp": True,  "udp": True,  "description": "Time Protocol"},
    53: {"tcp": True,  "udp": True,  "description": "DNS (Domain Name System)"},
    67: {"tcp": False, "udp": True,  "description": "BOOTP/DHCP Server"},
    68: {"tcp": False, "udp": True,  "description": "BOOTP/DHCP Client"},
    69: {"tcp": False, "udp": True,  "description": "TFTP (Trivial File Transfer Protocol)"},
    80: {"tcp": True,  "udp": False, "description": "HTTP (Hypertext Transfer Protocol)"},
    88: {"tcp": True,  "udp": True,  "description": "Kerberos Authentication System"},
    110: {"tcp": True,  "udp": False, "description": "POP3 (Post Office Protocol v3)"},
    111: {"tcp": True,  "udp": True,  "description": "RPC (Remote Procedure Call)"},
    123: {"tcp": False, "udp": True,  "description": "NTP (Network Time Protocol)"},
    135: {"tcp": True,  "udp": True,  "description": "DCE Endpoint Resolution"},
    137: {"tcp": False, "udp": True,  "description": "NetBIOS Name Service"},
    138: {"tcp": False, "udp": True,  "description": "NetBIOS Datagram Service"},
    139: {"tcp": True,  "udp": False, "description": "NetBIOS Session Service"},
    143: {"tcp": True,  "udp": False, "description": "IMAP (Internet Message Access Protocol)"},
    161: {"tcp": False, "udp": True,  "description": "SNMP (Simple Network Management Protocol)"},
    162: {"tcp": True,  "udp": True,  "description": "SNMPTRAP (SNMP Trap)"},
    179: {"tcp": True,  "udp": False, "description": "BGP (Border Gateway Protocol)"},
    194: {"tcp": True,  "udp": True,  "description": "IRC (Internet Relay Chat)"},
    389: {"tcp": True,  "udp": False, "description": "LDAP (Lightweight Directory Access Protocol)"},
    443: {"tcp": True,  "udp": False, "description": "HTTPS (Hypertext Transfer Protocol Secure)"},
    445: {"tcp": True,  "udp": False, "description": "Microsoft-DS (Active Directory, SMB)"},
    500: {"tcp": False, "udp": True,  "description": "ISAKMP (VPN Key Exchange for IPsec)"},
    514: {"tcp": True,  "udp": False, "description": "syslog (System Logging)"},
    520: {"tcp": False, "udp": True,  "description": "RIP (Routing Information Protocol)"},
    587: {"tcp": True,  "udp": False, "description": "SMTP (Email Submission)"},
    636: {"tcp": True,  "udp": False, "description": "LDAPS (Secure LDAP)"},
    989: {"tcp": True,  "udp": False, "description": "FTPS (FTP Secure Data)"},
    990: {"tcp": True,  "udp": False, "description": "FTPS (FTP Secure Control)"},
    993: {"tcp": True,  "udp": False, "description": "IMAPS (Secure IMAP)"},
    995: {"tcp": True,  "udp": False, "description": "POP3S (Secure POP3)"},
    1010: {"tcp": True,  "udp": False, "description": "ThinLinc (ThinLinc web-based administration interface)"},
}

def get_port_info(port):
    """Returns the service name and description of a given port"""
    try:
        service = socket.getservbyport(port)
    except OSError:
        service = "Unknown service"
    
    description = PORT_DESCRIPTIONS.get(port, "No description available")
    
    return service, description

if __name__ == "__main__":
    while True:
        user_input = input("Enter a port number (or type 'exit' to quit): ").strip()

        if user_input.lower() == "exit":
            print("Exiting program. Goodbye!")
            break
        
        if not user_input.isdigit():
            print("Please enter a valid numeric port.")
            continue

        port = int(user_input)
        service, description = get_port_info(port)
        print(f"\nPort: {port}\nService: {service}\nDescription: {description}\n")
