from selenium import webdriver

class Log_inForm():
    def __init__(self, driver, login, password, login_class, pass_class, btn_class):
        self.driver = driver
        self.login = login
        self.password = password
        self.login_class = login_class
        self.pass_class = pass_class
        self.btn_class = btn_class

        self.driver.maximize_window()


    def passData(self):
        login_form = self.driver.find_elements_by_class_name(self.login_class)
        login_form[0].send_keys(self.login)
        login_form[1].send_keys(self.password)


    def clickBtn(self):
        button = self.driver.find_element_by_class_name(self.btn_class)
        return button.click()
