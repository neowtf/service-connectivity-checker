import socket
import subprocess
import time
import dns.resolver

SERVICES = [
    "google.com", "facebook.com", "whatsapp.com", "instagram.com", "cloudflare.com",
    "openai.com", "drip.haus", "minepi.com", "k.gjacky.com", "semrush.com", "discord.com",
    "bixby.com", "demonware.net", "blizzard.com", "recruitee.com", "space.id",
    "usercentrics.eu", "sentry.io", "freepik.com", "chaos.com", "cpu-monkey.com",
    "geoimgr.com", "techpowerup.com", "sony.com", "king.com", "roboflow.com", "gettoby.com",
    "namshi.com", "yorku.ca", "ollama.com", "ssogateway.enscape3d.com", "northforge.ca",
    "parastorage.com", "webflow.com", "timedoctor.com", "tenor.com", "slooh.com",
    "galxe.com", "videvo.net", "allawntech.com", "services.adobe.com",
    "3dredboxstudio.com", "substancemaster.com", "lupaupscaler.com", "template.net",
    "dagshub.com", "tellent.com", "csr-racing.com", "fastly.com", "kmplayer.com",
    "kmpmedia.net", "egnyte.com", "hcaptcha.com", "revolut.com", "api.snapchat.com",
    "oasis-smartsim.com", "playground.com", "dreamy-room.org", "chaosgroup.com",
    "holvi.com", "unity.com"
]

# IPs from logs that failed connections
IPS = [
    "157.240.0.61", "149.154.167.41", "149.154.167.92", "188.114.96.0",
    "188.114.97.0", "57.144.249.33", "45.93.169.162", "185.56.137.2",
    "185.80.233.170", "37.143.86.95", "194.127.172.176", "47.241.18.77",
    "47.241.116.174"
]


def test_port(ip, port, timeout=4):
    try:
        sock = socket.socket()
        sock.settimeout(timeout)
        sock.connect((ip, port))
        sock.close()
        return True
    except:
        return False


def test_dns(domain):
    try:
        result = dns.resolver.resolve(domain, "A")
        return str(result[0])
    except:
        return None


def test_http(url, https=False, host=None):
    try:
        if https:
            cmd = ["curl", "-I", f"https://{url}",
                   "--max-time", "8", "-k", "-s"]
            if host:
                cmd = ["curl", "-H", f"Host: {host}", "-I",
                       f"https://{url}", "--max-time", "8", "-k", "-s"]
        else:
            cmd = ["curl", "-I", f"http://{url}", "--max-time", "8", "-s"]
            if host:
                cmd = ["curl", "-H", f"Host: {host}", "-I",
                       f"http://{url}", "--max-time", "8", "-s"]

        out = subprocess.run(cmd, capture_output=True)
        return out.returncode == 0
    except:
        return False


print("\n=================== FULL TEST START ===================\n")

# ---------- Test Domains ----------
for domain in SERVICES:
    print(f"\n🔍 Testing: {domain}")

    ip = test_dns(domain)
    if not ip:
        print("   ❌ DNS Error")
        continue

    print(f"   ✅ DNS OK → {ip}")

    # Port tests
    print(f"   {'✅' if test_port(ip, 80) else '❌'} Port 80 {'OK' if test_port(ip, 80) else 'BLOCKED'}")
    print(f"   {'✅' if test_port(ip, 443) else '❌'} Port 443 {'OK' if test_port(ip, 443) else 'BLOCKED'}")

    # HTTP / HTTPS tests
    print(
        f"   {'🌐 HTTP (curl) OK' if test_http(domain, False) else '❌ HTTP FAILED'}")
    print(
        f"   {'🔒 HTTPS (curl) OK' if test_http(domain, True) else '❌ HTTPS FAILED'}")

    print("--------------------------------------------------")

# ---------- Test IP Addresses ----------
print("\n=================== TESTING RAW IPs ===================\n")

for ip in IPS:
    print(f"\n🔍 Testing IP: {ip}")

    # Port tests
    print(f"   {'✅' if test_port(ip, 80) else '❌'} Port 80")
    print(f"   {'✅' if test_port(ip, 443) else '❌'} Port 443")

    # Test with SNI (fake HTTP Host)
    print(
        f"   🌐 HTTP (SNI bypass) → {'OK' if test_http(ip, False, host='example.com') else 'FAILED'}")
    print(
        f"   🔒 HTTPS (SNI) → {'OK' if test_http(ip, True, host='example.com') else 'FAILED'}")

    print("--------------------------------------------------")

print("\n==================== FULL TEST FINISHED ====================\n")
