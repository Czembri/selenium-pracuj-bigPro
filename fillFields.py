from selenium.webdriver.common.by import By # to get access to find_element_by_xpath but finally I used it another way
import time


class FillFields():
    def __init__(self, driver, text_class, workplace_class, btn_distance_class, li_value, text, workplace):
        self.driver = driver
        self.text_class = text_class
        self.worplace_class = workplace_class
        self.btn_distance_class = btn_distance_class
        self.li_value = li_value
        self.text = text
        self.workplace = workplace


    def typeKeyword(self):
        text_input = self.driver.find_element_by_class_name(self.text_class)
        return text_input.send_keys(self.text)

    def typeWorkplace(self):
        workplace_input = self.driver.find_element_by_class_name(self.worplace_class)
        workplace_input.send_keys(self.workplace)
        autocomplete = self.driver.find_element_by_class_name('autocomplete__item')
        return autocomplete.click()

    def chooseHowFar(self):
        how_far = self.driver.find_element_by_class_name(self.btn_distance_class).click()
        time.sleep(2)
        how_far_li = self.driver.find_element_by_xpath(f"//li[@value='{self.li_value}']") # using f string so you can choose the value whatever you want
        time.sleep(2)
        return how_far_li.click()

    def passData(self):
        button = self.driver.find_element_by_class_name('form-send__element') # button is just one so I could pass strictly the class name here :)
        return button.click()
