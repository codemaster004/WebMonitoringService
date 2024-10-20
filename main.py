from src.BaseScrapper import BaseScraper


if __name__ == '__main__':
    scraper = BaseScraper()
    scraper.send_request('https://www.x-kom.pl/')
    
