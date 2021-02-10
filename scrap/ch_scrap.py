from lib.ch.ch_scraper import ChScraper
from lib.ch import ch_config as config
from lib.ch.ch_options import ChOptions

if __name__ == '__main__':
    
    # Parse arguments and config
    opt = ChOptions(config)

    # Instantiate scraper instance
    scraper = ChScraper(jobs=opt.jobs,
                        url=opt.url,
                        driver_path=opt.args.driver,
                        submit_button=opt.submit_button,
                        dest=opt.args.dest)

    # Execute all scraping jobs
    scraper.scrap()
