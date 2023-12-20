import logging
import requests

from bs4 import BeautifulSoup
from typing import Union, Dict, List

logging.basicConfig(
    filename='Error.log',
    level=logging.INFO,
    format='%(asctime)s | [%(levelname)s]: %(message)s',
    datefmt='%m-%d-%Y / %I:%M:%S %p',
)

class HTTParser:
    def __init__(self, url:str=None, method:str=None, headers:dict=None, params:dict=None, payload:dict=None, response_format:str=None, browser_path:str=None, chromedriver_path:str=None):
        self.url = url
        self.method = method
        self.headers = headers
        self.params = params
        self.payload = payload
        self.response_format = response_format
        self.browser_path = browser_path
        self.chromedriver_path = chromedriver_path
        self.data = None

    def response(self) -> Union[Dict, List, str]:
        if self.response_format == "json":
            self.data = self._json_response()
        elif self.response_format == "html":
            self.data = self._html_response()
        elif self.response_format == "js":
            self.data = self._dynamic_response()
        else:
            logging.error(f"Invalid response format: {self.response_format}")
            raise ValueError(f"Invalid response format: {self.response_format}")
        if self.data:
            return self.data 
        else:
            logging.error(f"Error extracting data: {self.data}")
            raise HTTParserError(f"Error extracting data: {self.data}")

    def _json_response(self) -> Union[Dict, List]:
        try:
            headers = {
                'Content-Type':'application/json',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
            }
            if self.headers:
                headers = self.headers
            try:
                response = requests.request(
                    self.method.upper(), self.url, headers=headers, json=self.payload
                )
            except:
                response = requests.request(
                    self.method.upper(), self.url, headers=headers, data=self.payload
                )
            response.raise_for_status()
            return self._process_json_data(response)
        
        except requests.exceptions.RequestException as e:
            logging.error(f"Error extracting JSON data: {e}")
            raise HTTParserError(f"Error extracting JSON data: {e}")

    def _html_response(self) -> str:
        try:
            headers = { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" }
            if self.headers:
                headers = self.headers
            response = requests.request(
                self.method.upper(), self.url, headers=headers, params=self.params
            )
            response.raise_for_status()
            data = response.content
            return self._process_html_data(data)
        
        except requests.exceptions.RequestException as e:
            logging.error(f"Error extracting HTML data: {e}")
            raise HTTParserError(f"Error extracting HTML data: {e}")

    def _dynamic_response(self) -> Union[Dict, List, str]:
        if self.method.upper() != None and self.method.upper() != "" and self.method.upper() != "GET":
            logging.error(f"Invalid method [{self.method}] for Selenium. Only GET method is supported.")
            raise ValueError(f"Invalid method [{self.method}] for Selenium. Only GET method is supported.")
        
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service

        try:
            chromedriver_path = self.chromedriver_path
            browser_path = self.browser_path
            options = webdriver.ChromeOptions()
            if not self.headers:
                options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
            options.add_argument("--headless")
            options.page_load_strategy = 'normal'
            options.binary_location = browser_path
            s = Service(chromedriver_path)
            driver = webdriver.Chrome(service=s, options=options)

        except FileNotFoundError as e:
            logging.error(f"Invalid chromedriver and/or browser path: {e}")
            raise
        except Exception as e:
            logging.error(f"Error initializing Selenium WebDriver: {e}")
            raise
        
        try:
            driver.get(self.url)
            html = driver.page_source
            data = self._process_html_data(html)
        finally:
            driver.quit()
        return data

    def _process_json_data(self, data: Union[Dict, List]) -> Union[Dict, List]:
        data = data.json()
        return data

    def _process_html_data(self, html: bytes) -> str:
        data = BeautifulSoup(html, "html.parser")
        return data

class HTTParserError(Exception):
    pass