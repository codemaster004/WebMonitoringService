from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.scrapers.base_scraper import BaseScraper


class ScraperXKom(BaseScraper):
	
	def _get_next_page_button(self) -> WebElement:
		found = self._driver.find_element(By.CSS_SELECTOR, self.selectors['next'])
		return found if found.tag_name == 'a' else None
