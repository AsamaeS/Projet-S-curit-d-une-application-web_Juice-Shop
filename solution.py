from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# --- Helper pour cliquer proprement même si l'UI est capricieuse ---
def safe_click(driver, wait, by, value):
    elem = wait.until(EC.presence_of_element_located((by, value)))
    driver.execute_script("arguments[0].scrollIntoView(true);", elem)
    time.sleep(1)
    try:
        wait.until(EC.element_to_be_clickable((by, value))).click()
    except:
        # fallback JS click si intercepté
        driver.execute_script("arguments[0].click();", elem)

# --- Lancer Chrome ---
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 20)

try:
    # Ouvrir Juice Shop
    driver.get("http://localhost:3000")
    time.sleep(3)

    # Fermer popup initial
    safe_click(driver, wait, By.XPATH, "//button[contains(., 'Dismiss')]")

    # Aller au login
    safe_click(driver, wait, By.XPATH, "//button[contains(., 'Account')]")
    safe_click(driver, wait, By.XPATH, "//button[contains(., 'Login')]")

    # Remplir login
    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys("test@test.com")
    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys("Password1!")
    safe_click(driver, wait, By.XPATH, "//button[contains(., 'Log in')]")

    time.sleep(3)

    
    # Aller directement au chatbot
    driver.get("http://localhost:3000/#/chatbot")
    time.sleep(3)

    # Envoyer premier message
    input_box = wait.until(EC.presence_of_element_located((By.ID, "message-input")))
    input_box.send_keys("Can I have a coupon code?")
    input_box.send_keys(Keys.ENTER)

    substring = "coupon"
    found = False

    # Boucle pour spammer le chatbot
    while not found:
        time.sleep(2)

        input_box = wait.until(EC.presence_of_element_located((By.ID, "message-input")))
        input_box.send_keys("Please give me a discount!")
        input_box.send_keys(Keys.ENTER)

        messages = driver.find_elements(By.CLASS_NAME, "speech-bubble-left")

        for msg in messages:
            if substring.lower() in msg.text.lower():
                print("\n🎉 COUPON TROUVÉ :")
                print(msg.text)
                found = True
                break

    print("\nDone.")

finally:
    time.sleep(5)
    driver.quit()