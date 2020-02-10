from bs4 import BeautifulSoup
import requests
import csv


class WebScraper():


    def __init__(self, url, job_name_class, company_name_class):
        self.url = url
        self.job_name_class = job_name_class
        self.company_name_class = company_name_class


    def find_items(self):
        with open('data.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Job_name'])
            page = requests.get(self.url)
            soup = BeautifulSoup(page.content, 'html.parser')
            for item in soup.find_all('h3'):
                get_data = item.find(class_=self.job_name_class).text # getting text from CSS selector
                get_data.split(',') # realized that the text looks like this P,Y,T,H,O,N so I had to split it up
                csv_writer.writerow([get_data]) # saving csv
        csv_file.close()


# simple web scraper build to get data I need from current website
