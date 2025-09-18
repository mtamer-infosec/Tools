import socket
import requests

def get_local_ip():
    try:
        # Connect to an external host (Google DNS) to get the local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        return f"Error getting local IP: {e}"

def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org?format=text", timeout=5)
        return response.text
    except Exception as e:
        return f"Error getting public IP: {e}"

if __name__ == "__main__":
    print("Local IP :", get_local_ip())
    print("Public IP :", get_public_ip())
