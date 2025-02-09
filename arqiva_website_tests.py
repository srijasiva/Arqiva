import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os
import xmlrunner
import HtmlTestRunner
import chromedriver_autoinstaller

class ArqivaWebsiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chromedriver_autoinstaller.install()  # Automatically install the correct version of ChromeDriver
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://www.arqiva.com")
        cls.driver.maximize_window()
        if not os.path.exists('screenshots'):
            os.makedirs('screenshots')

    def test_home_page_load(self):
        self.assertIn("Arqiva", self.driver.title)
        self.driver.save_screenshot('screenshots/home_page.png')

    def test_home_page_no_footer(self):
        element_found = self.is_element_present(By.ID, "HomePageFooter")
        self.assertFalse(element_found)
        self.driver.save_screenshot('screenshots/home_page_no_footer.png')

    def test_main_tabs(self):
        tab_information = {
            "About": {"About Arqiva": "About Arqiva", "Arqiva Life": "Arqiva Life", "Leadership": "Our leaders", "Shareholders": "Our shareholders", "Corporate Responsibility": "Enabling a better world to flow", "Financial Reporting": "Financial Reporting"},
            "Media": {"Our Media Services": "Our media services", "TV": "Our television services", "TV Products": "Arqade", "Radio": "Our radio services"},
            "Utilities": {"Our Utilities Services": "Our utilities services", "Water metering": "Water metering services", "Managed connectivity": "Managed connectivity services", "Managed sensors": "Managed sensors", "Data analytics": "Data analytics"},
            "Satellite Data": {"Our satellite data services": "Our satellite data services", "Satellite Gateway": "Satellite gateway services", "Satellite Data Comms": "Satellite data comms"},
            "Careers": {"Careers at Arqiva": "Careers at Arqiva", "Why Arqiva?": "Why Arqiva?", "Graduates & Apprentices": "Graduates, interns and apprentices"}
        }

        for tab, sub_tabs in tab_information.items():
            self.verify_tab_and_sub_tabs(tab, sub_tabs)

        extra_tab_information = {
            "News & Views": "Latest news and views",
            "Contact": "Contact Arqiva"
        }
        for tab, expected_text in extra_tab_information.items():
            self.verify_tab(tab, expected_text)

    def verify_tab_and_sub_tabs(self, tab, sub_tabs):
        self.assertTrue(self.is_element_present(By.XPATH, f"//*[text()='{tab}']"))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//*[text()='{tab}']")))
        for sub_tab, expected_text in sub_tabs.items():
            self.driver.find_element(By.XPATH, f"//button[contains(text(), '{tab}')]").click()
            self.assertTrue(self.is_element_present(By.XPATH, f"//*[text()='{sub_tab}']"))
            self.driver.find_element(By.XPATH, f"//a[contains(text(), '{sub_tab}')]").click()
            self.assertTrue(self.is_element_present(By.XPATH, f"//h1[contains(text(), '{expected_text}')]"))
            self.driver.save_screenshot(f'screenshots/{tab}_{sub_tab}.png')

    def verify_tab(self, tab, expected_text):
        self.assertTrue(self.is_element_present(By.XPATH, f"//*[text()='{tab}']"))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//*[text()='{tab}']")))
        self.driver.find_element(By.XPATH, f"//a[contains(text(), '{tab}')]").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{expected_text}')]")))
        self.assertTrue(self.is_element_present(By.XPATH, f"//h1[contains(text(), '{expected_text}')]"))
        self.driver.save_screenshot(f'screenshots/{tab}.png')

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='results'))
