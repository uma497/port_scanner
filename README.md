# Port Scanner Project

## Overview

This project is a simple port scanner that allows users to check the status of ports on a specified host. It can be used to identify open, closed, or filtered ports, which is useful for network security assessments and troubleshooting.

## Features

- Scan a range of ports on any host (IP or domain).
- Uses multithreading for faster scanning.
- Displays real-time status of each port.
- Provides a summary of open ports.


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/uma497/port-scanner.py
   ```

2. Navigate to the project directory:

   ```bash
   cd port-scanner
   ```

3. Install any required libraries (if necessary):

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the scanner:

python port_scanner.py


Enter details when prompted:

=== Verbose Port Scanner ===
Enter target host (IP or domain): 127.0.0.1
Enter start port: 20
Enter end port: 100

📌 Example Output
Scanning 127.0.0.1 ...
Port 22: CLOSED
Port 80: OPEN
Port 443: CLOSED

Scan complete.
Open ports found: [80]

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
## Acknowledgments

- [Python](https://www.python.org/) for the programming language
- [Socket Programming](https://docs.python.org/3/library/socket.html) for network communication

## Contact

For any questions or feedback, please contact - umatomar497@gmail.com
