#!/bin/bash

echo "==============================================="
echo "     CheckNet - Service Connectivity Tester     "
echo "==============================================="
echo ""

# ----- 1. Update packages -----
echo "[1/5] Updating apt..."
apt update -y

# ----- 2. Install required packages -----
echo "[2/5] Installing required packages..."
apt install -y python3 python3-pip curl netcat

# ----- 3. Python modules -----
echo "[3/5] Installing Python modules..."
pip3 install dnspython

# ----- 4. Download the checker script -----
echo "[4/5] Downloading check_services.py ..."
curl -o /usr/local/bin/check_services.py https://raw.githubusercontent.com/neowtf/service-connectivity-checker/main/check_services.py

# (در نهایت یادت نره بالا USERNAME/REPO رو صحیح بذاری)

chmod +x /usr/local/bin/check_services.py

# ----- 5. Create 'checknet' CLI command -----
echo "[5/5] Creating checknet command..."

cat << 'EOF' > /usr/local/bin/checknet
#!/bin/bash
python3 /usr/local/bin/check_services.py
EOF

chmod +x /usr/local/bin/checknet

echo ""
echo "==============================================="
echo " Installation Complete!"
echo " You can now run the tool using:"
echo ""
echo "        checknet"
echo ""
echo "==============================================="
