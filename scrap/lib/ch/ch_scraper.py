from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import os
import sys

class ChScraper:

    '''
    class ChScraper

    defines a scraper instance for the Swiss Athletics results database
    '''

    def __init__(self, jobs, url, driver_path, submit_button, dest):

        '''
        ChScraper.__init__(self, jobs, url, driver, submit_button)

        constructor

        inputs:
        - jobs: dictionary containing the form arguments to load each page
            jobs = {
                $discipline: {
                    $category: [
                        {'id': $job_id, 
                         'year': ($year_field_id, $year_field_value),
                         'season': ($season_field_id, $season_field_value),
                         'category': ($category_field_id, $category_field_value),
                         'discipline': ($discipline_field_id, $discipline_field_value),
                         'list_type': ($lsit_type_field_id, $list_type_field_value),
                         'max_res': (max_res_field_id, $max_res_field_value)},
                        [...]
                    ]
                }
            }
        - url: form url
        - driverpath: path to chrome driver executable
        - submit_button: HTML id of the submit button
        - dest: destination folder in which to save the csv files

        output:
        - self: ChScraper instance
        '''

        self.url = url
        self.jobs = jobs
        self.submit_button = submit_button
        self.dest = dest

        self.sleep_time = 0.12
        self.max_retries = 6

        driver_path = os.path.join('.', driver_path)

        chrome_options = Options()  
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--log-level=3")

        print('\nConnecting ...\n')
        self.driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

    def to_iframe(self, url):

        '''
        ChSraper.get_form(self)

        connects driver to self.url to get the form
        '''

        self.driver.get(url)
        iframe = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "alabusContentIframe"))
        )
        self.driver.switch_to.frame(iframe)

    def rows_to_df(self, rows, col_names):

        '''
        ChScraper.row_to_df(self, rows, col_names)

        add rows to a pandas dataframe and return it

        inputs:
        - rows: Content of a table
        - col_names: Columns names of the table

        outputs:
        - job_df: dataframe containing the rows
        '''

        job_df = pd.DataFrame.from_dict({
            coln: {
                idx: None for idx in range(len(rows))
            } for coln in col_names
        })
        for idx, row in enumerate(rows):
            job_df.loc[idx] = row
        
        return job_df

    def set_table(self, job):

        '''
        ChScraper.set_table(self, job)

        Fill and submit the form of a given job to access the database

        input:
        - job: dictionary specifying fields, field ids and field values for 
               a given job
            job = { 'id': $job_id, 
                    'year': ($year_field_id, $year_field_value),
                    'season': ($season_field_id, $season_field_value),
                    'category': ($category_field_id, $category_field_value),
                    'discipline': ($discipline_field_id, $discipline_field_value),
                    'list_type': ($lsit_type_field_id, $list_type_field_value),
                    'max_res': (max_res_field_id, $max_res_field_value) }

        output:
        - 1: if success
        - 0: if some field could not be filled according to job
        '''

        self.to_iframe(self.url)
        print(f'{job["id"]}: Connection established')
        
        print(f'{job["id"]}: Filling form')

        for field, k in job.items():
            if field != 'id' and field != 'season':
                field_id, field_value = k
                try:
                    id_selector = self.driver.find_element_by_id(field_id)
                    id_selector.click()
                    time.sleep(self.sleep_time)
                    value_selector = self.driver.find_element_by_id(field_value)
                    value_selector.click()
                    time.sleep(self.sleep_time)
                except:
                    print(f'{job["id"]}: {field} not found')
                    return 0

        button = self.driver.find_element_by_id(self.submit_button)
        button.click()
        time.sleep(self.sleep_time)

        print(f'{job["id"]}: Form submitted.')

        return 1

    def get_row(self, row_obj, index, max_index, job_id):

        '''
        ChScraper.get_row(self, row_obj, index, max_index)

        read and store the content of a single row in the database

        input:
        - row_obj: selenium object containing the row
        - index: index of the row
        - max_index: total number of rows in the current table
        - job_id: id of the job (for printing)

        output:
        - row values in a list
        '''

        res = row_obj.find_elements_by_tag_name('td')
        print(f'{job_id}: {index+1}/{max_index} rows', end='\r')

        return [r.text for r in res[1:]]

    def scrap(self):

        '''
        ChScraper.scrap(self)

        execute all the jobs in self.jobs, stores the results in pandas
        dataframes and writes to csv
        '''

        for discipline in self.jobs.keys():
            for category in self.jobs[discipline].keys():
                df = pd.DataFrame()
                i = 0
                while i < len(self.jobs[discipline][category]):
                    job = self.jobs[discipline][category][i]                    
                    try:
                        status = self.set_table(job)
                        if not status:
                            k = 0
                            while k < self.max_retries and not status:
                                print(f'{job["id"]}: Retrying ...')
                                status = self.set_table(job)
                                k += 1
                            if not status:
                                print(f'{job["id"]}: Could not access table. skip job')
                                i += 1
                                continue

                        self.to_iframe(self.driver.current_url)
                        print(f'{job["id"]}: Table loaded')

                        tr_tags = self.driver.find_elements_by_tag_name('tr')
                        pos = tr_tags[0].text.find("naiss")
                        t = tr_tags[0].text[:pos-1]+'_'+tr_tags[0].text[pos:]
                        col_names = t.split()[1:]
                        col_names.extend(['discipline', 'catégorie'])

                        rows = []                        
                        for idx, row_obj in enumerate(tr_tags[1:]):
                            row = self.get_row(row_obj, idx, len(tr_tags[1:]), job["id"])
                            row.extend([discipline, category])
                            rows.append(row)

                        rows = [r for r in rows if len(r)==len(col_names)]
                        if len(rows)==0:
                            raise RuntimeError("")
                        
                        job_df = self.rows_to_df(rows, col_names)                        
                        df = pd.concat([df, job_df]).reset_index(drop=True)

                        print('\n')
                        i += 1
                    except KeyboardInterrupt:
                        sys.exit()
                    except:
                        print(f'{job["id"]}: An error occured. Retrying ...')
                        continue          

                if not os.path.isdir(os.path.join(self.dest, os.path.join(discipline))):
                    os.mkdir(os.path.join(self.dest, os.path.join(discipline)))
                df.to_csv(os.path.join(self.dest, os.path.join(discipline, f'{category}.csv')), index=False)
                print('{}-{}: Written to disk at `{}`\n'.format(
                    discipline, category, os.path.join(self.dest, os.path.join(discipline, f'{category}.csv'))
                ))
