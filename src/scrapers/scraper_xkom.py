from src.scrapers.base_scraper import BaseScraper


class ScraperXKom(BaseScraper):
	def __init__(self, selectors, dev: bool = False):
		BaseScraper.__init__(self, dev)
		
		self.selectors = selectors
	
	def scrap_page(self, url):
		print("HHIIIIIIII")
