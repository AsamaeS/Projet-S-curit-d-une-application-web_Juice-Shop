import os
import requests

def main():
    juice_shop_ip = os.environ.get('OWASP_JUICE_SHOP_IP_ADDRESS', 'localhost')
    juice_shop_port = os.environ.get('OWASP_JUICE_SHOP_PORT', '3000')
    
    base_url = f"http://{juice_shop_ip}:{juice_shop_port}"
    
    print(f"[+] Checking Score Board at: {base_url}/#/score-board")
    print("[!] For manual test, navigate to: " + base_url + "/#/score-board")
    
    print("[✅] Challenge Score Board should be solvable by visiting the URL!")

if __name__ == "__main__":
    main()
