from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class BaseScraper:
	_options = Options()
	_driver = None
	
	_selectors = {
		'tile': None,
		'price': None,
		'model': None,
	}
	
	def __init__(self, dev_mode: bool = False):
		if not dev_mode:
			self._options.add_argument("--headless")
		
		self._options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
		self._driver = webdriver.Firefox(options=self._options)
	
	def send_request(self, url):
		try:
			self._driver.get(url)
			self._driver.implicitly_wait(10)
		except Exception as e:
			print(f"Error fetching {url}: {e}")
			return None
	
	def scrap_page(self, url):
		print(f"Scraping {url}")
	
	@property
	def selectors(self):
		return self._selectors
	
	@selectors.setter
	def selectors(self, new_value):
		self._selectors = new_value
	
	def __del__(self):
		self._driver.close()
