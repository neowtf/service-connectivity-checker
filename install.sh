#!/bin/bash

echo "==============================================="
echo "   Service Connectivity Checker - Installer"
echo "==============================================="
echo ""

# ----- Update -----
echo "[1/5] Updating apt..."
apt update -y

# ----- Install required packages -----
echo "[2/5] Installing required packages..."
apt install -y python3 python3-pip curl netcat

# ----- Install Python modules -----
echo "[3/5] Installing Python modules..."
pip3 install dnspython

# ----- Download checker script -----
echo "[4/5] Downloading check_services.py ..."
curl -o /usr/local/bin/check_services.py https://raw.githubusercontent.com/USERNAME/REPO/main/check_services.py

# جایگزینی USERNAME و REPO با گیت شما  
# مثال:
# curl -o /usr/local/bin/check_services.py https://raw.githubusercontent.com/neowtf/service-connectivity-checker/main/check_services.py


# ----- Make executable -----
chmod +x /usr/local/bin/check_services.py

# ----- Done -----
echo ""
echo "==============================================="
echo " Installation Complete!"
echo " Run the script using:"
echo ""
echo "   python3 /usr/local/bin/check_services.py"
echo ""
echo "==============================================="
