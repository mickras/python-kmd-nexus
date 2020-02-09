# KMD Nexus Python Class
A Python Class for interacting with the KMD Nexus system, through Selenium and Chrome
webdriver. The class require the selenium package and the Chrome webdriver
(https://chromedriver.chromium.org/downloads) to run.

Example usage:
```
# In this example we log into KMD Nexus, change the account holders first- and
# lastname, log out and at the end, closing the browser session.

from selenium import webdriver

nexus_obj = KMDNexus()
KMDNexus.nexus_username = "my_username"
KMDNexus.nexus_password = "my_password"

driver = KMDNexus.NexusLogIn(nexus_obj)
KMDNexus.NexusChangeAccountName(nexus_obj, driver, first_name="Robotics", last_name="User")
KMDNexus.NexusLogOut(nexus_obj, driver)
KMDNexus.CloseBrowser(nexus_obj, driver)
```
