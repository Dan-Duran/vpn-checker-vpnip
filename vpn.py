import urllib.request
import json
import sys
import csv
import os
from datetime import datetime

# Your vpnapi.io token
TOKEN = 'ADD YOUR TOKEN HERE'
API_URL = 'https://vpnapi.io/api/'

def fetch_ip_info(ip):
    url = f"{API_URL}{ip}?key={TOKEN}"
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            return json.loads(data.decode())
    except urllib.error.URLError as e:
        print(f"Failed to retrieve data for {ip}: {e}")
        return None

def process_ip_list(file_path):
    items = read_ips_from_file(file_path)
    if not items:
        print(f"No valid IPs found in the file: {file_path}")
        return

    results = []
    for ip in items:
        data = fetch_ip_info(ip)
        if data:
            security = data.get('security', {})
            location = data.get('location', {})
            network = data.get('network', {})
            results.append(
                f"IP: {ip}\n"
                f"  VPN: {security.get('vpn', 'N/A')}, Proxy: {security.get('proxy', 'N/A')}, Tor: {security.get('tor', 'N/A')}, Relay: {security.get('relay', 'N/A')}\n"
                f"  City: {location.get('city', 'N/A')}, Region: {location.get('region', 'N/A')}, Country: {location.get('country', 'N/A')}, Continent: {location.get('continent', 'N/A')}\n"
                f"  Region Code: {location.get('region_code', 'N/A')}, Country Code: {location.get('country_code', 'N/A')}, Continent Code: {location.get('continent_code', 'N/A')}\n"
                f"  Latitude: {location.get('latitude', 'N/A')}, Longitude: {location.get('longitude', 'N/A')}\n"
                f"  Time Zone: {location.get('time_zone', 'N/A')}, Locale Code: {location.get('locale_code', 'N/A')}, Metro Code: {location.get('metro_code', 'N/A')}\n"
                f"  Is In European Union: {location.get('is_in_european_union', 'N/A')}\n"
                f"  Network: {network.get('network', 'N/A')}, ASN: {network.get('autonomous_system_number', 'N/A')}, ASO: {network.get('autonomous_system_organization', 'N/A')}\n"
            )

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"vpn-check-{timestamp}.txt")
    with open(output_path, 'w') as f:
        f.write("\n".join(results))

    print("\n".join(results))

def read_ips_from_file(file_path):
    items = []
    with open(file_path, 'r') as file:
        try:
            reader = csv.reader(file)
            for row in reader:
                for item in row:
                    item = item.strip()
                    if item and not item.startswith('#'):
                        items.append(item)
        except csv.Error:
            file.seek(0)
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    items.append(line)
    return items

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 vpnapi_check.py <input_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    process_ip_list(file_path)

if __name__ == "__main__":
    main()
