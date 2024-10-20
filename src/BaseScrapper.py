from selenium.webdriver.firefox.options import Options


class BaseScraper:
	headers = {"User-Agent": "Mozilla/5.0"}
	options = Options()
	driver = None
	
	def __init__(self, dev_mode: bool = False):
		if dev_mode:
			self.options.add_argument("--headless")
		self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
	
	def send_request(self, url):
		try:
			self.driver.get(url)
			print(self.driver.title)
			
			self.driver.implicitly_wait(10)
		except Exception as e:
			print(f"Error fetching {url}: {e}")
			return None
	
	def __del__(self):
		self.driver.close()
