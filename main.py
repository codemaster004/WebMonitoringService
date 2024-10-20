import src.scrapers as scrapers
import yaml


if __name__ == '__main__':
	# Load YML Config file
	with open('config.yml', 'r') as file:
		config = yaml.safe_load(file)
	
	# Read whether we are running the program in the dev environment (with gui)
	dev_mode = config['dev_mode']
	
	# Iterate over websites all websites we scrap data from
	for website in config['websites'].values():
		
		key = website['key']  # key for selecting scrapper
		my_scraper = scrapers.web_scrapers[key](website['selectors'], dev_mode)
		
		print(f"Beginning scraping data for {key}")
		
		# Scap separately for few targets on the same website
		for target in website['scrap_target']:
			data_file_path = target['data_file']  # Save values in data file under this path
			
			url = target['url']
			my_scraper.scrap_page(url)
			my_scraper.send_request(url)
