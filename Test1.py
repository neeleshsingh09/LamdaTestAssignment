from selenium import webdriver
import unittest
import urllib
import time
from selenium.webdriver.common.action_chains import ActionChains


class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Chrome(executable_path="..\Drivers\chromedriver.exe")
        cls.driver = webdriver.Chrome(
            r"C:\Users\Administrator\Downloads\ChromeDrivers\chromedriver_86\chromedriver.exe")
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

    def page_has_loaded(self):
       # self.log.info("Checking if {} page is loaded.".format(self.driver.current_url))
        page_state = self.driver.execute_script('return document.readyState;')
        return page_state == 'complete'

    def test_Login(self):
        self.driver.get("https://www.lambdatest.com/automation-demos/")
        element1 = self.driver.find_element_by_css_selector("*[class='cbtn btn_accept_ck']")
        if element1.is_displayed():
            element1.click()

        self.driver.find_element_by_name("name").send_keys("lambda")
        self.driver.find_element_by_name("password").send_keys("lambda123")

        element = self.driver.find_element_by_css_selector("[class='applynow']")

        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element.click()
        # self.driver.find_element_by_xpath("//*[@id='applyform']/div/button").click()

        self.driver.find_element_by_name("email").send_keys("neeleshsingh1987@gmail.com")
        self.driver.find_element_by_id("populate").click()
        time.sleep(3)

        alert_obj = self.driver.switch_to.alert
        alert_obj.accept()
        time.sleep(5)

        self.driver.find_element_by_id("month").click()
        self.driver.find_element_by_id("customer-service").click()
        # self.driver.find_element_by_id("preferred-payment").select_by_value('Wallets')
        self.driver.find_element_by_xpath("//select[@name='preferred-payment']/option[text()='Wallets']").click()
        self.driver.find_element_by_id("tried-ecom").click()
        time.sleep(3)

        self.driver.find_element_by_css_selector("*[id='slider'] + div > div:nth-child(9)").click()
        time.sleep(3)

        # Open a new window
        self.driver.execute_script("window.open('');")
        # Switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://www.lambdatest.com/selenium-automation")

        time.sleep(3)

        #Get image source
        image = self.driver.find_element_by_css_selector("img[src *= 'jenkins.svg']")
        src = image.get_attribute('src')
        self.driver.get('src')
        self.driver.save_screenshot('screenshot.png')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")
