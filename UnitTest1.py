"""
LambdaTest Selenium automation sample example
Configuration
----------
username: Username can be found at automation dashboard
accessToken:  AccessToken can be generated from automation dashboard or profile section

Result
-------
Execute Python Automation Tests on LambdaTest Distributed Selenium Grid
"""
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement


class LTAutomate(unittest.TestCase):
    """
    Setup remote driver
    Params
    ----------
    platform : Supported platform - (Windows 10, Windows 8.1, Windows 8, Windows 7,  macOS High Sierra, macOS Sierra, OS X El Capitan, OS X Yosemite, OS X Mavericks)
    browserName : Supported platform - (chrome, firefox, Internet Explorer, MicrosoftEdge)
    version :  Supported list of version can be found at https://www.lambdatest.com/capabilities-generator/

    Result
    -------
    """

    def setUp(self):
        # username: Username can be found at automation dashboard
        username = "neeleshsingh1987"
        # accessToken:  AccessToken can be generated from automation dashboard or profile section
        accessToken = "YtFwKoD04AiWrmmm6zPSEfG04WMs3HdVdzamLrNapj6qIDc45M"
        # gridUrl: gridUrl can be found at automation dashboard
        gridUrl = "hub.lambdatest.com/wd/hub"

        desired_cap = {
            'platform': "win10",
            'browserName': "chrome",
            'version': "67.0",
            # Resolution of machine
            "resolution": "1024x768",
            "name": "LambdaTest python assignment ",
            "build": "LambdaTest python assignment",
            "network": True,
            "video": True,
            "visual": True,
            "console": True,
        }

        # URL: https://{username}:{accessToken}@hub.lambdatest.com/wd/hub
        url = "https://" + username + ":" + accessToken + "@" + gridUrl

        print("Initiating remote driver on platform: " + desired_cap["platform"] + " browser: " + desired_cap[
            "browserName"] + " version: " + desired_cap["version"])
        self.driver = webdriver.Remote(
            desired_capabilities=desired_cap,
            command_executor=url
        )

    """
    Setup remote driver
    Params
    ----------
    Execute test:  navigate google.com search LambdaTest
    Result
    -------
    print title
    """

    def test_lamda_assignment(self):
        driver = self.driver
        print("Driver initiated successfully.  Navigate url")
        self.driver.get("https://www.lambdatest.com/automation-demos/")
        self.driver.maximize_window()

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

        # Get image source
        image = self.driver.find_element_by_css_selector("img[src *= 'jenkins.svg']")
        src = image.get_attribute('src')
        self.driver.get('src')
        self.driver.save_screenshot('screenshot.png')

        print("Printing title of current page :" + self.driver.title)
        self.driver.execute_script("lambda-status=passed")
        print("Requesting to mark test : pass")


"""
Quit selenium driver
"""


def tearDown(self):
    self.driver.close()
    self.driver.quit()
    print("Test completed")


if __name__ == "__main__":
    unittest.main()
