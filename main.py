from src.BaseScrapper import BaseScraper
import yaml


if __name__ == '__main__':
	with open('config.yml', 'r') as file:
		config = yaml.safe_load(file)
	
	print(config)

	scraper = BaseScraper()
	scraper.send_request('https://www.x-kom.pl/')
