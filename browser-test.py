from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

server ="http://127.0.0.1:4444/wd/hub"

driver = webdriver.Remote(command_executor=server,
    desired_capabilities=DesiredCapabilities.FIREFOX)

print("Loading page...")
driver.get("https://fedoramagazine.org/")
print("Loaded")
assert "Fedora" in driver.title
driver.save_screenshot("/tmp/screenshot.png")

driver.quit()
print("Done.")
