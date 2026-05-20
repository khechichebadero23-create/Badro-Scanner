# 🛡️ ShadowScan - Advanced Security Toolsuite

Welcome to the **ShadowScan** repository, an advanced and intelligent suite of security tools developed from scratch in Python. Designed for network scanning, data automation, penetration testing, and traffic analysis efficiently from mobile environments.

---

## 🚀 Available Tools in the Suite

### 1️⃣ ShadowScan - PortScanner
* **Description:** Scans target servers to discover active ports and running services, simulating Nmap core features.
* **Execution:** `python badro_scanner.py`

### 2️⃣ ShadowScan - DirFinder 🔓
* **Description:** An intelligent directory brute-forcing tool to discover hidden paths and admin panels on web targets.
* **Execution:** `python badro_dir.py`

### 3️⃣ ShadowScan - SubExtractor 🟢 *(Built from Scratch)*
* **Description:** A powerful DNS subdomain harvester built completely from scratch to extract active hosts and their IP mappings.
* **Execution:** `python shadow_sub.py`

### 4️⃣ ShadowScan - CryptoTicker 🪙
* **Description:** An automation script that connects to live global APIs to extract and analyze current cryptocurrency market prices in real-time.
* **Execution:** `python shadow_crypto.py`

### 5️⃣ ShadowScan - HashBreaker 🔑
* **Description:** A dedicated MD5 hash cracking tool designed to simulate brute-force attacks using custom wordlists efficiently.
* **Execution:** `python shadow_breaker.py`

### 6️⃣ ShadowScan - NetSniffer 📡
* **Description:** A TCP Server Edition packet analyzer that listens to internal local traffic, captures incoming connection signatures, and extracts raw data payloads.
* **Execution:** `python shadow_sniffer.py`

---

## 🛠️ Requirements & Installation

The suite is optimized to run with minimal external dependencies. Install the required `requests` library using:

```bash
sudo apt update && sudo apt install python3-requests -y

