from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

proxy = {"http":"http://edcguest:edcguest@172.31.100.29:3128/",
        "https":"http://edcguest:edcguest@172.31.100.29:3128/"}

def create_driver(name):
    if name == "Chrome":
        driver = webdriver.Chrome(
            executable_path="/home/aks/Documents/WebDevelopment/BrowserDrivers/chromedriver_linux64/chromedriver")
    elif name == "Firefox":
        driver = webdriver.Firefox(
            executable_path="/home/aks/Documents/WebDevelopment/BrowserDrivers/geckodriver-v0.24.0-linux64/geckodriver")
    return driver


# driver = create_driver("Firefox")
#
# driver.get("https://abhishek1103.github.io/aks.github.io/")
# print(driver.title)
#
# #driver.find_element_by_id('button_download_resume').click()
# driver.find_element_by_link_text('Download Resume').click()
#
# time.sleep(5)
#
# driver.close()

driver = create_driver("Chrome")
driver.get("https://www.instagram.com/advait_vaidya/")
driver.execute_script("window.scrollTo(0, 10000)")
a = []
time.sleep(10)
a = driver.find_elements_by_class_name("v1Nh3")

print("Number of sections found: ", len(a))

links = []

for element in a:
    l = element.find_elements_by_tag_name('a')
    for ln in l:
        try:
            links.append(ln.get_attribute('href'))
        except:
            pass

print("Number of links extracted: ", len(links))

image_links = []

for lnk in links:
    driver.get(lnk)
    divs = driver.find_elements_by_class_name("KL4Bh")
    for div in divs:
        img = div.find_element_by_tag_name('img')
        image_links.append(img.get_attribute('src'))

print(len(image_links))

with open('advait', 'w') as f:
    for il in image_links:
        f.write(il+"\n")

