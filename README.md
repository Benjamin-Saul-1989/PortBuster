# Port Information Lookup Tool

A simple command-line tool written in Python that allows users to query **Registered Ports (1024-49151)** to retrieve TCP/UDP availability and descriptions.

## Features
- Supports querying ports from **1024 to 49151**.
- Displays whether the port supports **TCP** and/or **UDP**.
- Provides a brief description of each port.
- Runs in an interactive loop, allowing users to query multiple ports.
- Users can exit the program by typing `exit`.

## Installation
### Prerequisites
- Python 3.x installed on your system.

### Clone the Repository
```bash
git clone https://github.com/yourusername/port-lookup-tool.git
cd port-lookup-tool
```

## Usage
### Run the Script
```bash
python port_lookup.py
```
### Example Input/Output
```bash
Enter a port number to get its information (type 'exit' to quit):
Port number: 3306
Port 3306: MySQL Database (TCP: True, UDP: False)

Port number: 8080
Port 8080: HTTP Alternative (TCP: True, UDP: False)

Port number: exit
Exiting the program...
```

## Contributing
Feel free to submit **pull requests** or open an **issue** if you find any missing ports or errors in descriptions.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Port descriptions sourced from **IANA** and other networking references.
- Inspired by the need for quick port information lookup.

---
**Author:** Your Name  
**GitHub:** [yourusername](https://github.com/yourusername)

