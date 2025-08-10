from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class EsuiteWebTest:
    def __init__(self):
        # ==== CONFIG ====
        self.base_url = "https://esuite.edot.id"  # Ganti dengan URL login kamu
        self.email = "it.qa@edot.id"
        self.password = "it.QA2025"
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 5)

    def run_test(self):
        try:
            self.driver.get(self.base_url)
            self.driver.maximize_window()

            # 1. Klik "Use Email or Username"
            use_email_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Use Email or Username')]"))
            )
            use_email_btn.click()
            time.sleep(1)  # jeda kecil untuk transisi

            # 2. Input Email
            email_input = self.wait.until(
                EC.visibility_of_element_located((By.NAME, "username"))
            )
            email_input.send_keys(self.email)

            # 3. Klik tombol login pertama
            login_btn1 = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/div/div[3]/div/button"))
            )
            login_btn1.click()
            time.sleep(1)

            # 4. Input Password
            password_input = self.wait.until(
                EC.visibility_of_element_located((By.NAME, "password"))
            )
            password_input.send_keys(self.password)

            # 5. Klik tombol login kedua
            login_btn2 = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/div/div[3]/div/button"))
            )
            login_btn2.click()

            # 6. Klik tombol all company
            all_company = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div/div[2]/div[2]/div[2]/button"))
            )
            all_company.click()
            time.sleep(1)

            # 7. Klik Add Company
            add_company = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div/div[1]/div/div/button[2]"))
            )
            add_company.click()
            time.sleep(1)

            # 8. Input Company Name
            input_company_name = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div/div/div/div[1]/div[2]/input"))
            )
            input_company_name.send_keys("testing")
            time.sleep(2)

            # 9. Input Email
            input_email = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div/div/div/div[1]/div[4]/div[1]/div/input"))
            )
            input_email.send_keys("test1@gmail.com")
            time.sleep(2)

            # 10. Input Nomer
            input_no = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div > main > div > div > div > div.flex.w-full.flex-col > div:nth-child(7) > div:nth-child(2) > div > div.ml-4.w-4\/5 > div > input"))
            )
            input_no.send_keys("8527937893")
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(4)

            # 11. Klik Type Industry
            klik_industry = self.wait.until(
                EC.element_to_be_clickable((By.ID, "radix-:r2e:"))
            )
            klik_industry.click()
            time.sleep(1)

        except Exception as e:
            print(f"Terjadi error: {e}")

        finally:
            self.driver.quit()

if __name__ == "__main__":
    test = EsuiteWebTest()
    test.run_test()