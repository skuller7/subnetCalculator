# Subnet Calculator

### This project is a CLI-based Subnet Calculator designed to help with CCNA subnetting.

### Inspired by an Udemy course I grabbed for $12 (shoutout to Mihai Catalin), this script includes some snippets from his repo, but it’s not a direct copy—I’ve made modifications.

Why This Exists?
Because I hate Programming

## Features
#### ✔️ Validates IP Addresses: Checks if an IP is Public, Private, APIPA, Loopback, or Special (Multicast/Experimental).

#### ✔️ User-Friendly: Simple CLI-based interface—just run and enter your IP!

#### ✔️ Validation Mechanisms: Ensures IP addresses are formatted correctly and octets don’t exceed valid ranges.

## Prerequisites & Usage

>Python 3.7+ is required (script won't work on Python 2 and may break on older versions).

> To run the script, navigate to the repo folder and execute:

>`python3 app.py`

## Phase 1: IP Address Validation

### The script first checks whether an IP address belongs to a valid range.
>Example: 192.168.1.0 is checked for four octets, ensuring no extra or missing numbers.
Incorrect inputs (e.g., 999.999.999.999 or 10.10.10) trigger an error message and exit.

### Example Validation Cases:
>127.0.0.10 → Loopback Address ✅
169.254.1.5 → APIPA (DHCP Auto-Assign) ✅
More features (Subnet Mask calculations, CIDR notation, etc.) might come in the future if I stop being lazy.