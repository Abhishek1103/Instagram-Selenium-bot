import requests
from selenium import webdriver
from time import sleep
from Const import EMAIL, PASSWORD


class InstaBot():
    def __init__(self, name):
        if name == "Chrome":
            self.driver = webdriver.Chrome(
                executable_path="/home/aks/Documents/WebDevelopment/BrowserDrivers/chromedriver_linux64/chromedriver")
        elif name == "Firefox":
            self.driver = webdriver.Firefox(
                executable_path="/home/aks/Documents/WebDevelopment/BrowserDrivers/geckodriver-v0.24.0-linux64/geckodriver")

    def login(self):
        self.driver.get("https://www.instagram.com/")
        sleep(3)
        print("hello")
        login_bt = self.driver.find_element_by_class_name('sqdOP')
        login_bt.click()
        sleep(2)
        input_email = self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input")
        input_pass = self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input")
        login = self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[3]/button")

        input_email.send_keys(EMAIL)
        input_pass.send_keys(PASSWORD)
        login.click()

    def notif_popup(self):
        sleep(2)
        pop = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]")
        bt = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")
        bt.click()

    def open_user(self, username):
        self.driver.get("https://www.instagram.com/"+username)
        print("User profile opened: "+username)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def iter_row(self, row):
        item = self.driver.find_elements_by_class_name("v1Nh3")

    def view_pics(self):
        sleep(2)
        items = self.driver.find_elements_by_class_name("v1Nh3")
        item = items[0]
        item.click()
        sleep(2)
        nxt = self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a")
        src_set = set()

        while True:
            try:
                article = self.driver.find_element_by_class_name("M9sTE")
            except:
                pass
            try:
                frame = article.find_element_by_class_name("KL4Bh")
            except:
                nxt.click()
                sleep(2)
                continue
            #frame = self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[1]/div/div/div[2]/div/div/div/div/ul/li[1]/div/div/div/div/div[1]/div[1]")
            # nxt_pic = self.driver.find_element_by_class_name("_6CZji")
            try:
                src = frame.find_element_by_tag_name("img").get_attribute('src')
            except:
                pass
            #src = frame.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[1]/div/div/div[2]/div/div/div/div/ul/li[1]/div/div/div/div/div[1]/div[1]/img").get_attribute('src')
            src_set.add(src)
            print(src)
            while True:
                try:
                    nxt_pic = self.driver.find_element_by_class_name("_6CZji")
                    nxt_pic.click()
                    article = self.driver.find_element_by_class_name("M9sTE")
                    frame = article.find_element_by_class_name("KL4Bh")
                    src = frame.find_element_by_tag_name("img").get_attribute('src')
                    src_set.add(src)
                    sleep(2)
                except:
                    break
            try:
                nxt.click()
                sleep(2)
            except:
                break;

        print(len(src_set))
        return src_set

    def saveImg(self, src, name):
        img_data = requests.get(src).content
        with open(name,'wb') as handler:
            handler.write(img_data)

    def download_pics(self, src_set):
        location = "/home/aks/Pictures/CPics/"
        base_name = ''
        num = 1
        for src in src_set:
            filename = location + base_name + str(num) + ".jpg"
            self.saveImg(src, filename)
            num += 1
            sleep(5)
