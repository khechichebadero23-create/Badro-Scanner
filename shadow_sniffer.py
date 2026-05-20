import socket
import sys

print("==================================================")
print("🛡️  ShadowScan - NetSniffer (Server Edition)")
print("==================================================")

# Define host and port to listen on (Localhost)
HOST = '127.0.0.1'
PORT = 9999

try:
    # Create a standard TCP Socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Allow immediate reuse of the port
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind the socket to our host and port
    server_socket.bind((HOST, PORT))
    
    # Start listening for incoming data packets
    server_socket.listen(5)
    print(f"[+] Sniffer Server started on {HOST}:{PORT}")
    print("[+] Waiting for live traffic data... Press Ctrl+C to stop.\n")
    
    packet_count = 0
    
    while True:
        # Accept incoming connection
        client_socket, client_address = server_socket.accept()
        packet_count += 1
        
        # Receive data from the connection
        raw_data = client_socket.recv(1024)
        decoded_data = raw_data.decode('utf-8', errors='ignore').strip()
        
        # Print captured packet logs smoothly
        print(f"📦 [Traffic #{packet_count}] Connection from: {client_address[0]}:{client_address[1]}")
        if decoded_data:
            print(f"   📜 Data Payload: {decoded_data}")
        print("──────────────────────────────────────────────────")
        
        # Close client socket
        client_socket.close()

except KeyboardInterrupt:
    print("\n[!] Sniffer Server stopped by user.")
    sys.exit(0)
except Exception as e:
    print(f"\n❌ An error occurred: {e}")
    sys.exit(1)

