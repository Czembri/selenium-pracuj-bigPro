from selenium import webdriver # webdriver to control the browser
from modules import Log_inForm # logging into page
import pickle # for cookies
import time # to wait for loading page content
from fillFields import FillFields # gets me access to job search inputs
from scraping.scraper import WebScraper # scraping data from the page

browser = webdriver.Chrome('C:/Users/czemb/OneDrive/Desktop/selenium_insta/chromedriver') # described in Readme file
url = 'https://login.pracuj.pl/'
browser.get(url)


#function which grab the password from .txt file, then create a dict where pass whole needed data to create Log in to the page
def userIndent(browser):
    with open('forms.txt', 'r') as file:
        for x in file:
            password = x
    users = [
        {
            'username' : 'email@gmail.com', # your email
            'password' : password, # your password from .txt file
            'login_class' : 'egkVq', # CSS selector of username input
            'pass_class' : 'egkVq', # CSS selector of password input
            'btn_class' : '_19V_Q', # CSS selector of button
        },
    ]

    user = Log_inForm(browser, users[0]['username'], users[0]['password'], users[0]['login_class'], users[0]['pass_class'], users[0]['btn_class']) # passing data into a class I've created and described
    # remember to get index of list and than pass a dictionary key :)
    user.passData() # this method pass data into inputs
    user.clickBtn() # click submit button

    return time.sleep(5) # it allows to load website content - I have really slow an Internet connection :)


userIndent(browser) # calling function and passing webdriver link into it
pickle.dump(browser.get_cookies() , open("QuoraCookies.pkl","wb")) # This part of code saves cookies, it allows you to stay logged while changing sessions

time.sleep(5)

for cookie in pickle.load(open("QuoraCookies.pkl", "rb")): # reading cookies for next url I am gonna to use
    if 'expiry' in cookie: # I needed to delete this key to get access to the directory
        del cookie['expiry']
    browser.add_cookie(cookie)
browser.get('https://www.pracuj.pl/apps/#/konto/rekomendowane-oferty') # passing another url
job_offers = browser.find_element_by_class_name('header__nav_list_item_link')
job_offers.click()

time.sleep(5)

click_no = browser.find_element_by_id('customNotificationPromptNoButton').click() # I got a message from the website so I had to answer it :)

def find_a_job(browser): # function thanks what I can pass text into inputs and search for a job
    search_conditions = [
        {
            'text_class':'keyword__field',
            'workplace_class':'workplace__field',
            'btn_distance_class':'radius__trigger',
            'li_value':'10',
            'text':'Python developer',
            'workplace':'Poznań'

        }
    ]

    searchin_1 = FillFields(browser, search_conditions[0]['text_class'], search_conditions[0]['workplace_class'],
                            search_conditions[0]['btn_distance_class'], search_conditions[0]['li_value'], search_conditions[0]['text'],
                            search_conditions[0]['workplace']
                            )
    searchin_1.typeKeyword()
    time.sleep(5)
    searchin_1.typeWorkplace()
    time.sleep(5)
    searchin_1.chooseHowFar()
    time.sleep(5)
    return searchin_1.passData()

find_a_job(browser)

current_url = browser.current_url # getting url from the current page I am on

def web_scrapper(current_url):
    scrap_data = [
        {
            'job_class':'offer-details__title-link',
            'company_class':'offer-company__name'
        }
    ]
    data = WebScraper(current_url, scrap_data[0]['job_class'], scrap_data[0]['company_class'])
    write_to_csv = data.find_items() # using BS4 to get job names from the page *edit finally I did not use a company class which allows me to get the company name of the job
    # I just realized that This is useles

web_scrapper(current_url)
