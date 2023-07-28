from selenium.webdriver.common.by import By
from selenium import webdriver


class Attribute_Options:
    class_name: By.CLASS_NAME
    css_selector: By.CSS_SELECTOR
    id: By.ID
    name: By.NAME
    tag_name : By.TAG_NAME

class Browser_Agents:
    chrome: webdriver.Chrome
    firefox: webdriver.Firefox
    safari: webdriver.Safari
    edge: webdriver.Edge
    chromium_edge: webdriver.ChromiumEdge