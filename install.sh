#!/bin/bash

echo "=========================================="
echo "   Service Connectivity Checker Installer"
echo "=========================================="
sleep 1

# Update system
echo "[1/5] Updating system..."
apt update -y >/dev/null 2>&1

# Install dependencies
echo "[2/5] Installing required packages..."
apt install -y python3 python3-pip curl netcat >/dev/null 2>&1

# Install dnspython
echo "[3/5] Installing Python dependencies..."
pip3 install dnspython >/dev/null 2>&1

# Create directory
mkdir -p /opt/service-checker

# Download latest script
echo "[4/5] Downloading connectivity checker..."
curl -s -o /opt/service-checker/check.py \
https://raw.githubusercontent.com/neowtf/service-connectivity-checker/main/check_services.py

chmod +x /opt/service-checker/check.py

# Add launcher command
echo "[5/5] Creating shortcut command: checknet"
echo "python3 /opt/service-checker/check.py" >/usr/local/bin/checknet
chmod +x /usr/local/bin/checknet

echo ""
echo "=========================================="
echo " Installation Complete!"
echo " Run with:   checknet"
echo "=========================================="
