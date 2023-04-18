# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
# from urllib.parse import quote
# import os
# from selenium.webdriver.chrome.service import Service

# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# options.add_argument("--profile-directory=Default")
# options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")

# os.system("")
# os.environ["WDM_LOG_LEVEL"] = "0"
# class style():
#     BLACK = '\033[30m'
#     RED = '\033[31m'
#     GREEN = '\033[32m'
#     YELLOW = '\033[33m'
#     BLUE = '\033[34m'
#     MAGENTA = '\033[35m'
#     CYAN = '\033[36m'
#     WHITE = '\033[37m'
#     UNDERLINE = '\033[4m'
#     RESET = '\033[0m'


# f = open("message.txt", "r", encoding="utf8")
# message = f.read()
# f.close()

# print(style.YELLOW + '\nThis is your message-')
# print(style.GREEN + message)
# print("\n" + style.RESET)
# message = quote(message)

# numbers = []
# f = open("num.txt", "r")
# for line in f.read().splitlines():
# 	if line.strip() != "":
# 		numbers.append(line.strip())
# f.close()
# total_number=len(numbers)
# print(style.RED + 'We found ' + str(total_number) + ' numbers in the file' + style.RESET)
# delay = 30

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# print('Once your browser opens up sign in to web whatsapp')
# driver.get('https://web.whatsapp.com')
# input(style.MAGENTA + "AFTER logging into Whatsapp Web is complete and your chats are visible, press ENTER..." + style.RESET)
# for idx, number in enumerate(numbers):
# 	number = number.strip()
# 	if number == "":
# 		continue
# 	print(style.YELLOW + '{}/{} => Sending message to {}.'.format((idx+1), total_number, number) + style.RESET)
# 	try:
# 		url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
# 		sent = False
# 		for i in range(3):
# 			if not sent:
# 				driver.get(url)
# 				try:
# 					click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='compose-btn-send']")))
# 				except Exception as e:
# 					print(style.RED + f"\nFailed to send message to: {number}, retry ({i+1}/3)")
# 					print("Make sure your phone and computer is connected to the internet.")
# 					print("If there is an alert, please dismiss it." + style.RESET)
		
# 				else:
# 					sleep(1)
# 					click_btn.click()
# 					sent=True
# 					sleep(3)
# 					print(style.GREEN + 'Message sent to: ' + number + style.RESET)
# 	except Exception as e:
# 		print(style.RED + 'Failed to send message to ' + number + str(e) + style.RESET)
		
# driver.close()

# import time

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
# from urllib.parse import quote
# import os
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains

# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# options.add_argument("--profile-directory=Default")
# options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")

# send_msg_time = 10

# os.system("")
# os.environ["WDM_LOG_LEVEL"] = "0"

# class style():
#     BLACK = '\033[30m'
#     RED = '\033[31m'
#     GREEN = '\033[32m'
#     YELLOW = '\033[33m'
#     BLUE = '\033[34m'
#     MAGENTA = '\033[35m'
#     CYAN = '\033[36m'
#     WHITE = '\033[37m'
#     UNDERLINE = '\033[4m'
#     RESET = '\033[0m'


# f = open("message.txt", "r", encoding="utf8")
# message = f.read()
# f.close()

# print(style.YELLOW + '\nThis is your message-')
# print(style.GREEN + message)
# print("\n" + style.RESET)
# message = quote(message)

# numbers = []
# f = open("num.txt", "r")
# for line in f.read().splitlines():
#     if line.strip() != "":
#         numbers.append(line.strip())
# f.close()
# total_number = len(numbers)
# print(style.RED + 'We found ' + str(total_number) + ' numbers in the file' + style.RESET)
# delay = 30

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# print('Once your browser opens up sign in to web whatsapp')
# driver.get('https://web.whatsapp.com')
# sleep(7)

# # input(style.MAGENTA + "AFTER logging into Whatsapp Web is complete and your chats are visible, press ENTER..." + style.RESET)

# for idx, number in enumerate(numbers):
#     number = number.strip()
#     if number == "":
#         continue
#     print(style.YELLOW + '{}/{} => Sending message to {}.'.format((idx+1), total_number, number) + style.RESET)
#     try:
#         url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
        
#         driver.get(url)
#         sleep(5)
#         attachment_box = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//div[@title = "Attach"]')))
#         attachment_box.click()
#         image_box = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')))
#         image_path = os.path.abspath('src/hello.png') # replace with the path to your image file
#         image_box.send_keys(image_path)
#         sleep(5)
#         send_button = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send"]')))
#         send_button.click()
#         sleep(7)
#         print(style.GREEN + 'Message sent to: ' + number + style.RESET)
#     except Exception as e:
#         print(style.RED + 'Failed to send message to ' + number + str(e) + style.RESET)

# driver.close()
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from urllib.parse import quote
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")

send_msg_time = 10

os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

# prompt user for message file path
message_file_path = input("Please enter the path to the message file: ")
if not os.path.isfile(message_file_path):
    print("Invalid message file path!")
    sys.exit()

# prompt user for number file path
number_file_path = input("Please enter the path to the number file: ")
if not os.path.isfile(number_file_path):
    print("Invalid number file path!")
    sys.exit()
image_path = input("Please enter the path to the image file: ")

f = open(message_file_path, "r", encoding="utf8")
message = f.read()
f.close()

print(style.YELLOW + '\nThis is your message-')
print(style.GREEN + message)
print("\n" + style.RESET)
message = quote(message)

numbers = []
f = open(number_file_path, "r")
for line in f.read().splitlines():
    if line.strip() != "":
        numbers.append(line.strip())
f.close()
total_number = len(numbers)
print(style.RED + 'We found ' + str(total_number) + ' numbers in the file' + style.RESET)
delay = 30

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
print('Once your browser opens up sign in to web whatsapp')
driver.get('https://web.whatsapp.com')
input(style.MAGENTA + "AFTER logging into Whatsapp Web is complete and your chats are visible, press ENTER..." + style.RESET)

# input(style.MAGENTA + "AFTER logging into Whatsapp Web is complete and your chats are visible, press ENTER..." + style.RESET)

for idx, number in enumerate(numbers):
    number = number.strip()
    if number == "":
        continue
    print(style.YELLOW + '{}/{} => Sending message to {}.'.format((idx+1), total_number, number) + style.RESET)
    try:
        url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
        
        driver.get(url)
        sleep(5)
        attachment_box = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//div[@title = "Attach"]')))
        attachment_box.click()
        image_box = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')))
        image_box.send_keys(image_path)
        sleep(5)
        send_button = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send"]')))
        send_button.click()
        sleep(7)
        print(style.GREEN + 'Message sent to: ' + number + style.RESET)
    except Exception as e:
        print(style.RED + 'Failed to send message to ' + number + str(e) + style.RESET)

driver.close()


