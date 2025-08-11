from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class EworkMobileTest:
    def __init__(self):
        # 1. Config Desired Capabilities
        desired_caps = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "deviceName": "Xiaomi 220333QPG",
            "appPackage": "id.edot.ework",
            "appActivity": "id.edot.onboarding.ui.splash.SplashScreenActivity",
            "noReset": False,
            "newCommandTimeout": 300
        }

        # 2. UiAutomator2Options
        options = UiAutomator2Options().load_capabilities(desired_caps)

        # 3. Jalankan Appium Driver
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

    def create_customer(self):
        pelangganBaru_menu = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='id.edot.ework:id/img_menu'])[5]"))
        )
        pelangganBaru_menu.click()
        time.sleep(2)

        # BASIC
        regis_pelanggan_baru = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/tvRegister']"))
        )
        regis_pelanggan_baru.click()
        time.sleep(1)

        nama_toko = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ID, "id.edot.ework:id/et_outlet_name"))
        )
        nama_toko.send_keys("eDOT Task")
        time.sleep(1)

        no_telp = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ID, "id.edot.ework:id/et_outlet_phone"))
        )
        no_telp.send_keys("8567918777")
        time.sleep(1)

        masukan_email = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ID, "id.edot.ework:id/et_outlet_email"))
        )
        masukan_email.send_keys("mobileAuotomation@gmail.com")
        time.sleep(1)

        personal_contact = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ID, "id.edot.ework:id/et_contact_person"))
        )
        personal_contact.send_keys("PT. Elektronik Distribusi Otomatisasi Terkemuka")
        self.driver.find_element(by="-android uiautomator", value='new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(10)')

        tipe_saluran = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ID, "id.edot.ework:id/et_channel"))
        )
        tipe_saluran.click()
        time.sleep(1)

        general_trade = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/tvName' and @text='General Trade (GT)']"))
        )
        general_trade.click()
        time.sleep(1)

        tipe_toko = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ID, "id.edot.ework:id/et_outlet_type"))
        )
        tipe_toko.click()
        time.sleep(1)

        retailer_large = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH,
                                        "//android.widget.TextView[@resource-id='id.edot.ework:id/tvName' and @text='Retailer Large']"))
        )
        retailer_large.click()
        time.sleep(1)

        lanjut = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ID, "id.edot.ework:id/button_text"))
        )
        lanjut.click()
        time.sleep(2)
        print("✅Halaman Basic berhasil dibuat")

        # LOKASI
        jenis_alamat = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ID, "id.edot.ework:id/et_address_type"))
        )
        jenis_alamat.click()
        time.sleep(1)

        delivery_address = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/tvName' and @text='Delivery Address']"))
        )
        delivery_address.click()
        time.sleep(1)

        # Scroll sedikit ke bawah
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollForward()')
        time.sleep(1)

        alamat_lokasi = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ID, "id.edot.ework:id/etAddress"))
        )
        alamat_lokasi.send_keys("Jl. Banda Aceh No. 20")
        time.sleep(1)

        provinsi = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.EditText[@resource-id='id.edot.ework:id/etInput' and @text='Pilih Provinsi']"))
        )
        provinsi.click()
        time.sleep(1)

        pili_provinsi = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/txt_name' and @text='GORONTALO']"))
        )
        pili_provinsi.click()
        time.sleep(1)

        kota = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.EditText[@resource-id='id.edot.ework:id/etInput' and @text='Pilih Kota']"))
        )
        kota.click()
        time.sleep(1)

        pilih_kota = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/txt_name' and @text='KAB BONE BOLANGO']"))
        )
        pilih_kota.click()
        time.sleep(1)

        kecamatan = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.EditText[@resource-id='id.edot.ework:id/etInput' and @text='Pilih Kecamatan']"))
        )
        kecamatan.click()
        time.sleep(1)

        klik_kecamatan = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/txt_name' and @text='BONE RAYA']"))
        )
        klik_kecamatan.click()
        time.sleep(1)

        # Scroll lagi
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollForward()')
        time.sleep(1)

        kelurahan = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.EditText[@resource-id='id.edot.ework:id/etInput' and @text='Pilih Kelurahan']"))
        )
        kelurahan.click()
        time.sleep(1)

        klik_kelurahan = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/txt_name' and @text='PELITA JAYA']"))
        )
        klik_kelurahan.click()
        time.sleep(1)

        kodePos = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.EditText[@resource-id='id.edot.ework:id/etInput' and @text='Pilih Kode pos']"))
        )
        kodePos.click()
        time.sleep(1)

        klik_kodePos = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ID, "id.edot.ework:id/txt_name"))
        )
        klik_kodePos.click()
        time.sleep(1)

        lanjut2 = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.Button[@resource-id='id.edot.ework:id/button_text' and @text='Lanjutkan']"))
        )
        lanjut2.click()
        time.sleep(2)
        print("✅Halaman Lokasi berhasil dibuat")

        # Dokumen
        permissionDoc = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ID, "id.edot.ework:id/btn_positive"))
        )
        permissionDoc.click()
        time.sleep(1)

        permissionDoc2 = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button"))
        )
        permissionDoc2.click()
        time.sleep(1)

        permissionDoc3 = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button"))
        )
        permissionDoc3.click()
        time.sleep(1)

        ktp = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ID, "id.edot.ework:id/etInput"))
        )
        ktp.send_keys("1912312324393888")
        time.sleep(1)

        unggah_berkas = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.Button[@resource-id='id.edot.ework:id/button_text' and @text='Unggah Berkas']"))
        )
        unggah_berkas.click()
        time.sleep(1)

        camera = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ID, "id.edot.ework:id/btn_capture"))
        )
        camera.click()
        time.sleep(1)

        daftar = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.Button[@resource-id='id.edot.ework:id/button_text' and @text='Daftar']"))
        )
        daftar.click()
        time.sleep(2)

        klikTtd = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ID, "id.edot.ework:id/signature_view"))
        )
        klikTtd.click()
        time.sleep(1)

        daftar2 = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.Button[@resource-id='id.edot.ework:id/button_text' and @text='Daftar']"))
        )
        daftar2.click()
        time.sleep(2)

        ya = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.Button[@resource-id='id.edot.ework:id/button_text' and @text='Ya']"))
        )
        ya.click()
        print("✅Pelanggan Baru berhasil dibuat")
        time.sleep(5)

    def run_test(self):
        try:
            self.login()
            time.sleep(2)
            self.create_customer()
        finally:
            self.driver.quit()

if __name__ == "__main__":
    test = EworkMobileTest()
    test.run_test()
