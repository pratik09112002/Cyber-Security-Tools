import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host: str, port: int, timeout: float = 1.0) -> bool:
    """Return True if port is open, False otherwise."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((host, port))
            return True
        except (socket.timeout, ConnectionRefusedError, OSError):
            return False


def scan_range(host: str, start_port: int, end_port: int, workers: int = 100):
    print(f"\nScanning {host} from port {start_port} to {end_port} ...")
    open_ports = []

    def worker(p):
        if scan_port(host, p):
            print(f"[+] Port {p} is OPEN")
            open_ports.append(p)

    with ThreadPoolExecutor(max_workers=workers) as executor:
        executor.map(worker, range(start_port, end_port + 1))

    print("\nScan complete.")
    if open_ports:
        print("Open ports:", ", ".join(map(str, sorted(open_ports))))
    else:
        print("No open ports found in this range.")


def main():
    print("=== Simple Port Scanner ===")
    host = input("Enter target host (IP or domain): ").strip()
    start = int(input("Start port: ").strip())
    end = int(input("End port: ").strip())

    if start < 1 or end > 65535 or start > end:
        print("Invalid port range. Use 1–65535 and start <= end.")
        return

    scan_range(host, start, end)


if __name__ == "__main__":
    main()
