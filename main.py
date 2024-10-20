import yaml
import pandas as pd

import src.scrapers as scrapers
from src.exeptions import UnsupportedSelectorsFormat


if __name__ == '__main__':
	# Load YML Config file
	with open('config.yml', 'r') as file:
		config = yaml.safe_load(file)
	
	# Read whether we are running the program in the dev environment (with gui)
	try:
		dev_mode = config['dev_mode']
	except KeyError:
		print("WARNING: Missing 'dev_mode' key in config.yml")
		dev_mode = False
	
	# Iterate over websites all websites we scrap data from
	for website in config['websites'].values():
		# Try setting up a scraper for a website, in case of failing skip to next website
		try:
			key = website['key']  # key for selecting scrapper
			my_scraper = scrapers.web_scrapers[key](website['selectors'], dev_mode)
		except KeyError as e:
			print(f"ERROR: Key error while setting up the scrapper: {e}")
			print("INFO: Skipping to the next webpage.")
			continue
		except UnsupportedSelectorsFormat as e:
			print(f"ERROR: {e}")
			print("INFO: Skipping to the next webpage.")
			continue
		
		print(f"INFO: Beginning scraping data for {key}")
		
		# Scap separately for few targets on the same website
		for target in website['scrap_target']:
			data_file_path = target['data_file']  # Save values in data file under this path
			
			url = target['url']
			scrap_data = my_scraper.scrap_page(url)
			
			df = pd.DataFrame(scrap_data)
			df.to_csv(data_file_path, index=False)
			
			print(f"INFO: Scraping data saved to {data_file_path}")
