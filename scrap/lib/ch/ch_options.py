import argparse
import os

class ChOptions:

    def __init__(self, config):

        self.config = config
        self.url = self.config.url
        self.submit_button = self.config.submit_button

        self.parser = self.get_parser()
        self.args = self.parser.parse_args()

        self.jobs = self.format_config()

    def file_path(self, x):

        '''
        ChOptions.file_path(self, x)

        Check that the input x is a valid file path

        inputs:
        - x: Input to validate

        outputs:
        - x: Valid output

        errors:
        - argparse.ArgumentTypeError: x is an invalid file path
        '''

        if not os.path.isfile(x):
            raise argparse.ArgumentTypeError(f'Value `{x}` is not a valid file path')

        return x

    def dir_path(self, x):

        '''
        ChOptions.directory(self, x)

        Check that the input x is a valid directory, if not, creates it

        inputs:
        - x: Input to validate

        outputs:
        - x: Valid output
        '''

        if not os.path.isdir(x):
            os.mkdir(x)

        return x

    def get_parser(self):

        athl_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

        p = argparse.ArgumentParser()

        p.add_argument('--driver', type=self.file_path, required=False, default='chromedriver',
                       help='path to chromedriver exectuable')
        p.add_argument('--dest', type=self.dir_path, required=False, default=os.path.join(athl_root, os.path.join('data', 'ch')),
                       help='path to chromedriver exectuable')

        return p

    def format_config(self):

        disciplines = self.config.disciplines
        categories = ['H', 'F']
        years = self.config.years

        jobs = {
            discipline: {
                category: [] for category in categories
            } for discipline in disciplines
        }

        for discipline in disciplines:
            for category in categories:
                cat = self.config.men_category if category == 'H' else self.config.women_category
                catname = 'men' if category == 'H' else 'women'
                for year in years:
                    job = {
                        'id': f'{discipline}-{category}-{year}',
                        'year': (self.config.fields['year'], self.config.year_id(year)),
                        'season': (self.config.fields['season'], self.config.season),
                        'category': (self.config.fields['category'], cat),
                        'discipline': (self.config.fields['discipline'], self.config.discipline_cfg[str(year)][catname][discipline]),
                        'list_type': (self.config.fields['list_type'], self.config.list_type),
                        'max_res': (self.config.fields['max_res'], self.config.max_res)
                    }
                    jobs[discipline][category].append(job)

        return jobs
