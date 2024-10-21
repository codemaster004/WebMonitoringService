from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.scrapers.base_scraper import BaseScraper


class ScraperXKom(BaseScraper):
	
	def _get_next_page_button(self) -> WebElement:
		""" Finds and returns the Next button on the page or None if not found """
		found = self._driver.find_element(By.CSS_SELECTOR, self.selectors['next'])
		# On X-kom the button can always be found on the page,
		# however when it is the last page of pagination, it is not an <a> just a <span>
		return found if found.tag_name == 'a' else None
