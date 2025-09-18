# Local and Public IP Address Finder

This Python script retrieves both the **local IP address** of your
machine (within your local network) and the **public IP address** (as
seen from the internet).

------------------------------------------------------------------------

## 📌 Features

-   Gets the **local IP** using Python's `socket` module.
-   Gets the **public IP** using the `ipify` API.
-   Handles errors gracefully.
-   Works on Linux, Windows, and macOS.

------------------------------------------------------------------------

## 📂 Code Explanation

### Local IP Address

``` python
import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    s.close()
    return local_ip
```

-   Creates a UDP socket and connects to Google DNS (8.8.8.8).
-   No data is sent; it's just used to determine which network
    interface/IP your system uses.
-   Extracts the local IP using `getsockname()`.

### Public IP Address

``` python
import requests

def get_public_ip():
    response = requests.get("https://api.ipify.org?format=text", timeout=5)
    return response.text
```

-   Uses the free ipify service to fetch your public IP.
-   Returns the public IP as plain text.

------------------------------------------------------------------------

## ⚡ Requirements

-   `requests` library (install with `pip install requests`)

------------------------------------------------------------------------

## ✅ Notes

1.  Local IP is useful to identify your machine inside your home/office
    network.
2.  Public IP is useful to check how your ISP/router exposes your
    connection to the internet.
3.  If behind a VPN, the public IP will show the VPN's address.
