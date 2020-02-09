"""
Class for interacting with KMD Nexus through Selenium webdriver (Chrome webdriver). 
The Chrome webdriver is not included in the repository, but can be downloaded here:
https://chromedriver.chromium.org/downloads

"""
from selenium import webdriver
import time

class KMDNexus:
    # General settings related to the KMD Nexus account that should
    # by used by the class.
    nexus_url               = "https://mycompany.nexus.kmd.dk"
    web_driver_path_chrome  = "C:\\selenium\\chromedriver.exe"
    nexus_username          = ""
    nexus_password          = ""

    def __init__(self, headless=False):
        pass

    def NexusLogIn(self, headless=False):
        """
        Funtion that initiate the webdriver, opens the log in page for KMD Nexus,
        and logging into the system. If the argument "headless" is set to True,
        the browser will run in headless mode. This is not fully tested, and
        not all KMD Nexus functions might work in headless mode.

        Before calling the function, the KMD Nexus account credentials should
        be defined. Example:

        KMDNexus.nexus_username = "mykmdusername"
        KMDNexus.nexus_password = "mykmdpassword"
        """
        options = webdriver.ChromeOptions()
        options.add_argument('--log-level=3')
        if headless:
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')

        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(self.web_driver_path_chrome, options=options)

        # Load KMD Nexus login page
        driver.get(self.nexus_url)

        # Fill in username and password, and clik the log-in button
        driver.find_element_by_id("j_username").send_keys(self.nexus_username)
        driver.find_element_by_id("j_password").send_keys(self.nexus_password)
        driver.find_element_by_id("login-button").click()

        return driver

    def NexusChangeAccountName(self, driver, **kwargs):

        """
        Function for changing the name of the account holder on the logged in account.
        Name and initials arguments are all optional, however, it's
        required to use named parameters when calling the function. Example:

        KMDNexus.NexusChangeAccountName(nexus_obj, driver, first_name="Robotics")

        the following parameters is accepted:
        * first_name
        * middle_name
        * last_name
        * initials

        Only the parameters given, will be updated on the account in KMD Nexus.
        If e.g. paramter for last_name is not given, the lastname on the account
        will be unchanged.
        """
        driver.get(self.nexus_url + "/dialog/rbac$professionalEdit")
        time.sleep(2)

        arg_list = {}
        changes = False
        arg_list["first_name"] = "firstName"
        arg_list["middle_name"] = "middleName"
        arg_list["last_name"] = "lastName"
        arg_list["initials"] = "initials"

        for key, value in kwargs.items():
            if key in arg_list:
                driver.find_element_by_id(arg_list[key]).clear()
                driver.find_element_by_id(arg_list[key]).send_keys(value)
                changes = True

        if changes:
            driver.find_element_by_xpath('//button[contains(text(), "Gem og luk")]').click()


    def NexusLogOut(self, driver):
        driver.get(self.nexus_url)
        time.sleep(2)
        driver.find_element_by_id("nexus-core-logout-btn").click()

    def CloseBrowser(self, driver):
        driver.close()
        driver.quit()


if __name__ == "__main__":
    #Example usage:
    nexus_obj = KMDNexus()
    KMDNexus.nexus_username = "mykmdusername"
    KMDNexus.nexus_password = "mykmdpassword"

    driver = KMDNexus.NexusLogIn(nexus_obj)
    time.sleep(3)

    KMDNexus.NexusChangeAccountName(nexus_obj, driver, first_name="Robotics", last_name="User")
    time.sleep(5)

    KMDNexus.NexusLogOut(nexus_obj, driver)
    time.sleep(3)
    KMDNexus.CloseBrowser(nexus_obj, driver)
