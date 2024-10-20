import src.scrapers as scrapers
import yaml


if __name__ == '__main__':
	# Load YML Config file
	with open('config.yml', 'r') as file:
		config = yaml.safe_load(file)
	
	# Read whether we are running the program in the dev environment (with gui)
	dev_mode = config['dev_mode']
	
	for website in config['websites'].values():
		
		key = website['key']
		print(f"Beginning scraping data for {key}")
		my_scraper = scrapers.web_scrapers[key](website['selectors'], dev_mode)
		
		for target in website['scrap_target']:
			data_file = target['data_file']
			url = target['url']
			my_scraper.scrap_page(url)
			my_scraper.send_request(url)
