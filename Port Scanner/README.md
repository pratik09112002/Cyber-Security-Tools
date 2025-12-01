# Port Scanner

## Overview
This tool scans a target host for open TCP ports within a user-defined range. 
It helps identify exposed network services and is useful for learning basic network reconnaissance and security assessment concepts.

## Features
- Scans a single target (IP or domain) over a custom port range.
- Uses multi-threading to speed up scanning.[web:52]
- Displays all detected open ports in a simple CLI output.

## Requirements
- Python 3.x
- Standard library only (no external dependencies).

## Usage
Run the script with Python

Then provide:
- Target host (e.g., `127.0.0.1` or `scanme.nmap.org`)
- Start port (e.g., `1`)
- End port (e.g., `1024`)
The tool will list any open ports found in the specified range.

## Legal Notice
Use this tool only on systems and networks you own or have explicit permission to test. Unauthorized scanning may violate laws and policies.
