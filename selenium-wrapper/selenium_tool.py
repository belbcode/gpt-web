from selenium import webdriver
import time

from selenium_options import Attribute_Options, Browser_Agents
from makeid import makeid

from langchain.tools import BaseTool



class SeleniumWrapper:
    def __init__(self, **kwargs):

        specified_agent = kwargs['browser_agent']

        if specified_agent:
            self.driver = Browser_Agents[specified_agent]()
            return
        
        self.driver = webdriver.Chrome()

    def NavigateTool(self):
        driver = self.driver

        class Navigate(BaseTool):

            name="Webpage Navigate"
            description="Useful for when you need to navigate to a webpage and read it's text contents."

            def _run(self, url: str):
                driver.get(url)
                html_el = driver.find_element(Attribute_Options.tag_name, 'html')
                return f"Web-content: {html_el.text}\n HTML Element is currently stored and may be manipulated by pageparsing tools"
                
            def _arun(self, url: str):
                raise NotImplementedError("This tool does not support async")
            
        return Navigate
        

    def open_page(self, url):
        # https://www.youtube.com/watch?v=Xz514u4V_ts        
        self.driver.get(url)
        self.currentPage = self.driver.page_source
        time.sleep(2) #switch to better waiting mechanism
        updatedhtml = self.driver.execute_script("return document.documentElement.outerHTML;")
        self.currentPage = updatedhtml
        return f"The {url} has been opened and shown to the viewer and its contents have been saved locally and are accessible via your pageparsing tools"

    def select_element(self, attribute : Attribute_Options, attribute_value: str = ""):
        print(attribute, attribute_value)
        return attribute, attribute_value
        # if self.currentPage == None:
        #     return "You need to make sure a webpage is opened and it's contents have been saved before you access its' contents."
        # element = self.driver.find_element(Attribute_Options[attribute], attribute_value)
        # element_refernce = self._makeid()
        # self.elements[element_refernce] = element
        # return f"The element has been saved locally can be accessed by this key: {element_refernce}"

        # if not attribute or not attribute_value:
        #     return "This tool requires 2 inputs an attribute type and attribute value."
            # return ""
    def quit(self):
        self.driver.quit()
        # attribute_options = {
        #     "class_name": By.CLASS_NAME,
        #     "css_selector": By.CSS_SELECTOR,
        #     "id": By.ID,
        #     "name": By.NAME,
        #     "tag_name" : By.TAG_NAME
        # }

    def clear(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
        if self.elements:
            self.elements = {}
        if self.currentPage:
            self.currentPage = None
        return "Class instance has been cleared..."
        
        
    def _is_intantiated(self):
        if self.driver == None:
            self.driver = webdriver.Chrome()
        return



    