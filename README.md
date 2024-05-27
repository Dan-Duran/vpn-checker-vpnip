# VPN API IP Checker

This Python script allows you to check a list of IP addresses using the vpnapi.io API. The script fetches detailed information about each IP address, including security information, location, and network details.

## Features

- Fetches detailed information about IP addresses from vpnapi.io.
- Provides security details (VPN, Proxy, Tor, Relay).
- Provides location details (City, Region, Country, Continent, Latitude, Longitude, etc.).
- Provides network details (Network, ASN, ASO).
- Outputs results to a timestamped file in the `output` directory.

## Prerequisites

- Python 3.6 or later.
- An API key from [vpnapi.io](https://vpnapi.io/).

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Dan-Duran/vpn-checker-vpnip.git
    cd vpn-api-ip-checker
    ```

2. Save your API key in the script:

    Open `vpnapi_check.py` and replace the placeholder `YOUR_API_KEY` with your actual API key.

    ```python
    TOKEN = 'YOUR_API_KEY'
    ```

## Usage

1. Prepare your input file with IP addresses:

    Create a file (e.g., `input.txt`) and add IP addresses to it, one per line. You can also use any file format such as CSV.

    Example `input.txt`:

    ```plaintext
    # Add your IP list here (one IP address per line)
    8.8.8.8
    123.456.789.0
    etc
    ```

2. Run the script:

    ```bash
    python3 vpn.py input.txt
    ```

3. Check the output:

    The script will print the results to the terminal and save them to a timestamped file in the `output` directory.

    Example output file: `output/vpn-check-YYYY-MM-DD_HH-MM-SS.txt`

    Example output:

    ```plaintext
    IP: 8.8.8.8
      VPN: False, Proxy: False, Tor: False, Relay: False
      City: , Region: , Country: United States, Continent: North America
      Region Code: , Country Code: US, Continent Code: NA
      Latitude: 37.7510, Longitude: -97.8220
      Time Zone: America/Chicago, Locale Code: en, Metro Code: 
      Is In European Union: False
      Network: 8.8.8.0/24, ASN: AS15169, ASO: GOOGLE
    ```

## File Structure

```plaintext
vpn-checker-vpnip/
├── input.txt
├── output/
│   └── vpn-check-YYYY-MM-DD_HH-MM-SS.txt
├── vpn.py
└── README.md
```
## Parameters Explained

### Security
- **VPN**: Determines if IP address is a VPN.
- **Proxy**: Determines if IP address is a Proxy.
- **Tor**: Determines if IP address is a Tor Node.
- **Relay**: Determines if IP address is a Relay (e.g., iCloud Private Relay).

### Location
- **City**: Displays the approximate city of the IP address location.
- **Region**: Displays the approximate region or state of the IP address location.
- **Country**: Displays the approximate country of the IP address location.
- **Continent**: Displays the approximate continent of the IP address location.
- **Region Code**: Displays the IP address ISO 3166-1 country code.
- **Country Code**: Displays the IP address region/state code.
- **Continent Code**: Displays the IP address continent code.
- **Latitude**: Displays the latitude of the IP address.
- **Longitude**: Displays the longitude of the IP address.
- **Time Zone**: Displays the approximate time zone of the IP address.
- **Locale Code**: Determines the regional language based on the IP address location.
- **Metro Code**: Displays the metro code based on the IP address location (for US IP addresses).
- **Is In European Union**: Determines if the IP address is located within the European Union.

### Network
- **Network**: Displays which network the IP address belongs to.
- **Autonomous System Number (ASN)**: Displays the autonomous system number of the network.
- **Autonomous System Organization (ASO)**: Displays the organization that manages the network.

### Contributing
Contributions are welcome! Please submit a pull request with any improvements or additions.

### License
This project is licensed under the MIT License - see the LICENSE file for details.


