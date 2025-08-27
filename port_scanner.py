#!/usr/bin/env python3
import socket
import concurrent.futures

def scan_port(host: str, port: int, timeout: float = 1.0) -> str:
    """Check if a port is open or closed."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((host, port))
            if result == 0:
                return "OPEN"
            else:
                return "CLOSED"
    except Exception:
        return "ERROR"

def scan_ports(host: str, ports: range):
    print(f"Scanning {host} ...")
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        future_to_port = {executor.submit(scan_port, host, port): port for port in ports}
        for future in concurrent.futures.as_completed(future_to_port):
            port = future_to_port[future]
            status = future.result()
            results[port] = status
            print(f"Port {port}: {status}")
    return results

def main():
    print("=== Verbose Port Scanner ===")
    host = input("Enter target host (IP or domain): ").strip()
    start = int(input("Enter start port: "))
    end = int(input("Enter end port: "))
    ports = range(start, end + 1)

    results = scan_ports(host, ports)

    # Print summary
    open_ports = [p for p, status in results.items() if status == "OPEN"]
    print("\nScan complete.")
    if open_ports:
        print("Open ports found:", open_ports)
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
