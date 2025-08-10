from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class EworkMobileTest:
    def __init__(self):
        desired_caps = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "deviceName": "Xiaomi 220333QPG",  # ganti dengan nama device real
            "appPackage": "id.edot.ework",
            "appActivity": "id.edot.onboarding.ui.splash.SplashScreenActivity",
            "noReset": False,
            "newCommandTimeout": 300
        }

        options = UiAutomator2Options().load_capabilities(desired_caps)
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
        self.wait = WebDriverWait(self.driver, 20)

    def login(self):
        id_perusahaan = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ID, "id.edot.ework:id/tv_company_id"))
        )
        id_perusahaan.send_keys("5049209")
        time.sleep(1)

        input_email = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ID, "id.edot.ework:id/tv_username"))
        )
        input_email.send_keys("qatestsalesman")
        time.sleep(1)

        input_password = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ID, "id.edot.ework:id/tv_password"))
        )
        input_password.send_keys("it.QA2025")
        time.sleep(1)

        masuk_button = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ID, "id.edot.ework:id/button_text"))
        )
        masuk_button.click()
        time.sleep(3)

        persmission_element = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button"))
        )
        persmission_element.click()
        print("✅Login berhasil")
        time.sleep(2)

    def tampilData(self):
        master_outlet = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='id.edot.ework:id/img_menu'])[3]"))
        )
        master_outlet.click()
        time.sleep(2)

        cari = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ID, "id.edot.ework:id/btn_search"))
        )
        cari.click()
        time.sleep(1)

        input_pencarian = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ID, "id.edot.ework:id/et_search"))
        )
        input_pencarian.send_keys("eDOT Task")
        time.sleep(3)

        lihat_detail = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ID, "id.edot.ework:id/outlet_action"))
        )
        lihat_detail.click()
        time.sleep(10)

        tutup = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ID, "id.edot.ework:id/btnClose"))
        )
        tutup.click()
        time.sleep(5)
        print("✅Berhasil menampilkan data yang baru saja dibuat")

    def run_test(self):
        try:
            self.login()
            # beri delay lebih lama untuk menunggu transisi halaman selesai
            time.sleep(3)
            self.tampilData()
        finally:
            self.driver.quit()

if __name__ == "__main__":
    test = EworkMobileTest()
    test.run_test()
