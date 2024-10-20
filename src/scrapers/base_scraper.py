import re
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webelement import WebElement

from src.exeptions import UnsupportedSelectorsFormat


class BaseScraper:
	_options = Options()  # Options for the driver, required by selenium
	_driver = None  # Web browser driver to be set in the __init__ after configuring options
	_selectors = {}  # CSS selectors for various parts of scraping, e.g., price, title, etc.
	
	def __init__(self, selectors, dev_mode: bool = False):
		# In Developer Mode, the GUI of the browser will be visible for easier testing
		if not dev_mode:
			# In Production, selenium will run without opening any windows for performance
			self._options.add_argument("--headless")
		
		# Validate and set the CSS selectors if provided
		if self.__validate_selectors(selectors):
			self.selectors = selectors
		
		# Set the browser agent to simulate a Windows computer running Firefox
		self._options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
		# Create the driver for selenium with set options
		self._driver = webdriver.Firefox(options=self._options)
	
	def scrap_page(self, url):
		""" Main method to scrape a page and returns the collected data """
		self._open_page(url)  # Open first page of the target
		self._accept_cookies()  # Accept cookies to get rid of the popup
		
		collected_data = []  # List for the all the collected data from scraping
		self._visit_all_pagination(collected_data)  # Start collecting the data and visiting next pagination's
		return collected_data
	
	def _visit_all_pagination(self, collected_data):
		""" Visits all pages by finding and clicking the 'next' button and collects data """
		while True:
			sleep(3)  # Allow UI to load
			offer_cards = self._get_all_offer_cards()
			# Collect data from each offer card and append to collected_data
			for card in offer_cards:
				collected_data.append({
					'price': self._get_price(card),
					'title': self._get_title(card),
					'info': self._get_info(card),
				})
			# Attempt to find and click the next page button
			next_page_button = self._get_next_page_button()
			if next_page_button is None:
				break  # Exit if there is no next page button
			next_page_button.click()
	
	def _open_page(self, url):
		""" Opens the given URL in the browser """
		try:
			self._driver.get(url)
			# Wait implicitly for elements to be ready
			self._driver.implicitly_wait(5)
		except Exception as e:
			print(f"ERROR: While fetching {url} - {e}")
	
	def _accept_cookies(self):
		""" Handles cookie acceptance if required by the site """
		self._driver.implicitly_wait(3)
		self._driver.find_element(By.CSS_SELECTOR, self.selectors['cookie']).click()
		self._driver.implicitly_wait(1)
	
	def _get_all_offer_cards(self):
		""" Retrieves all offer cards from the current page """
		return self._driver.find_elements(By.CSS_SELECTOR, self.selectors['card'])
	
	def _get_price(self, offer_card: WebElement):
		""" Extracts and returns the price from an offer card """
		return self._get_numeric_value(offer_card, self.selectors['price']) / 100
	
	def _get_title(self, offer_card: WebElement):
		""" Extracts and returns the title from an offer card """
		return self._get_text_value(offer_card, self.selectors['title'])
	
	def _get_info(self, offer_card: WebElement):
		""" Extracts and returns additional info from an offer card """
		return self._get_text_value(offer_card, self.selectors['info'])
	
	def _get_next_page_button(self) -> WebElement:
		""" Finds and returns the Next button on the page or None if not found """
		found = self._driver.find_elements(By.CSS_SELECTOR, self.selectors['next'])
		return None if found == [] else found[0]
	
	@property
	def selectors(self):
		""" Property getter for selectors """
		return self._selectors
	
	@selectors.setter
	def selectors(self, new_value):
		""" Property setter for selectors """
		self._selectors = new_value
	
	@staticmethod
	def _get_numeric_value(offer_card: WebElement, css_selector: str):
		""" Extracts a numeric value from an offer card """
		found = offer_card.find_elements(By.CSS_SELECTOR, css_selector)
		return None if found == [] else BaseScraper._to_int(found[0].text)
	
	@staticmethod
	def _get_text_value(offer_card: WebElement, css_selector: str):
		""" Extracts a text value from an offer card """
		found = offer_card.find_elements(By.CSS_SELECTOR, css_selector)
		return None if found == [] else found[0].text
	
	@staticmethod
	def _to_int(text: str):
		# Remove all non-digit characters using Regex
		# Converts the cleaned text to an integer
		cleaned_text = re.sub(r'\D', '', text)
		return int(cleaned_text)
	
	@staticmethod
	def __validate_selectors(selector_dict):
		""" Validates the provided selectors to ensure all required fields are present """
		if selector_dict is None:
			raise UnsupportedSelectorsFormat('Selectors cannot be None')
		if not isinstance(selector_dict, dict):
			raise UnsupportedSelectorsFormat('Selectors must be a dict')
		if selector_dict == {}:
			raise UnsupportedSelectorsFormat('Selectors cannot be empty')
		required_fields = ['cookie', 'card', 'title', 'price', 'info', 'next']
		for field in required_fields:
			if field not in selector_dict:
				raise UnsupportedSelectorsFormat(f'Selectors must contain `{field}` field')
		return True
	
	def __del__(self):
		""" Destructor to ensure the browser is properly closed """
		self._driver.close()
