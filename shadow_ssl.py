import socket
import ssl
import sys
from datetime import datetime

print("==================================================")
print("🛡️  ShadowScan - SSL/TLS Certificate Analyzer")
print("==================================================")

# Get target domain from user
target_host = input("[+] Enter Target Domain (e.g., google.com): ").strip()

print(f"\n[+] Connecting to {target_host} on port 443 to fetch SSL details...\n")

try:
    # Create a standard socket connection
    base_socket = socket.create_connection((target_host, 443), timeout=5)
    
    # Create a secure SSL context
    context = ssl.create_default_context()
    
    # Wrap the socket with SSL to establish a secure handshake
    secure_socket = context.wrap_socket(base_socket, server_hostname=target_host)
    
    # Extract the certificate information dictionary
    cert = secure_socket.getpeercert()
    
    print("🟩 [SSL Certificate Fetched Successfully!]")
    print("──────────────────────────────────────────────────")
    
    # Parse Issuer Information
    issuer = dict(x[0] for x in cert['issuer'])
    print(f"🏢 Issued By (Organization): {issuer.get('organizationName', 'Unknown')}")
    print(f"🌍 Common Name (CN): {issuer.get('commonName', 'Unknown')}")
    
    # Parse Validity Dates
    # Leaving them as naive datetimes for easy comparison
    date_format = r"%b %d %H:%M:%S %Y %Z"
    valid_from = datetime.strptime(cert['notBefore'], date_format).replace(tzinfo=None)
    valid_to = datetime.strptime(cert['notAfter'], date_format).replace(tzinfo=None)
    
    print(f"📅 Valid From: {valid_from}")
    print(f"📅 Expires On: {valid_to}")
    
    # Secure and clean current time fetching without warnings
    current_time = datetime.now().replace(tzinfo=None)
    
    # Compare naive datetimes smoothly
    if current_time > valid_to:
        print("⚠️  Status: EXPIRED! (Insecure Connection)")
    else:
        print("✅ Status: VALID & ACTIVE")
        
    print("──────────────────────────────────────────────────")
    
    # Close connections safely
    secure_socket.close()

except socket.timeout:
    print("❌ Error: Connection timed out. Target might be down or blocking port 443.")
except ssl.SSLError as ssl_err:
    print(f"❌ SSL Error: Could not establish a secure handshake. ({ssl_err})")
except Exception as e:
    print(f"❌ An error occurred: {e}")

print("\n--- SSL Analysis Completed ---")

