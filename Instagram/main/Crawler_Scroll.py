from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import signal, sys
import requests
import threading

proxy = {"http":"http://username:password@<proxy address>:<proxy port>/",
        "https":"http://username:password@<proxy address>:<proxy port>/"}



def download_file(set_of_l, file_path):
    print("File Path: ", file_path)
    print("Number of links received: ", len(set_of_l))
    i = 0
    sett = set_of_l.copy()
    for il in sett:
        try:
            r = requests.get(il)
            filename = file_path + "/img" + i + ".jpg"
            i = i + 1
            with open(filename, 'wb') as f:
                f.write(r.content)
        except:
            pass

def create_driver(name):
    if name == "Chrome":
        driver = webdriver.Chrome(
            executable_path="<Path to the driver executable>")
    elif name == "Firefox":
        driver = webdriver.Firefox(
            executable_path="<Path to the driver executable>")
    return driver


# driver = create_driver("Firefox")
#
# driver.get("<url>")
# print(driver.title)
#
# #driver.find_element_by_id('button_download_resume').click()
# driver.find_element_by_link_text('Download Resume').click()
#
# time.sleep(5)
#
# driver.close()

set_of_links = set()


def signal_handler(sig, frame):
    print("\nRECIEVED SIGINT")
    with open('file', 'a') as f:
        for il in set_of_links:
            try:
                f.write(il + "\n")
            except:
                pass
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


#profile_link = input("Enter the profile link of the account: ")
#file_path = input("Enter the path of directory: ")
file_path = "<path_to_download_dir>"
driver = create_driver("Chrome")
driver.get("https://www.instagram.com/<instagram_handle>/")
#driver.get(profile_link)

SCROLL_PAUSE_TIME = 2
last_height = driver.execute_script("return document.body.scrollHeight")

n = 0
a = set()
ii = 1
i = 0
while n < 25:
    try:
        driver.get("https://www.instagram.com/<instagram_handle>/")
    except:
        break
    for j in range(ii):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        # if new_height == last_height:
        #     break
        # last_height = new_height
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        # if new_height == last_height:
        #     print("Reached the end")
        #     break
        last_height = new_height

    a = driver.find_elements_by_class_name("v1Nh3")
    print("Number of sections found: ", len(a))
    n = n+1
    ii = ii + 1

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
            try:
                img = div.find_element_by_tag_name('img')
                image_links.append(img.get_attribute('src'))
                set_of_links.add(img.get_attribute('src'))
            except:
                pass

    print(len(set_of_links))
    # if len(set_of_links) > 50:
    #     set_of_links_copy = set_of_links.copy()
    #     set_of_links.clear()
    #     print("File Path: ", file_path)
    #     print("Number of links received: ", len(set_of_links_copy))
    #     sett = set_of_links_copy.copy()
    #     for il in sett:
    #         try:
    #             print("Requesting the image: ",str(il))
    #             r = requests.get(str(il), proxies=proxy)
    #             filename = file_path + "/img" + i + ".jpg"
    #             print(filename)
    #             i = i + 1
    #             with open(filename, 'wb') as f:
    #                 f.write(r.content)
    #         except Exception as e:
    #             print("Exception: ", str(e))
    #             pass


    # with open('advait', 'a') as f:
    #     for il in image_links:
    #         try:
    #             f.write(il+"\n")
    #         except:
    #             pass


with open('file', 'a') as f:
    for il in set_of_links:
        try:
            f.write(il+"\n")
        except:
            pass





