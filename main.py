
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
#message_file_path = input("Please enter the path to the message file: ")
message_file_path = "input/message.txt"
number_file_path = "input/numbers.txt"
image_path = "input/image.jpg"
if not os.path.isfile(message_file_path):
    path = input("""Can not find the message file in input directory. Please make 
sure you have a message.txt file in input directory and press enter
or enter your own path if the file is located somewhere else.

Enter alternate path or press enter to exit: """)
    if path == "":
        print("\nOperation stopped by USER : " + style.RED + "Could not find message file/altenate path not provided" + style.RESET)
        sys.exit()

    else:
        message_file_path = path
print(style.GREEN + "Message file found." + style.RESET)

# prompt user for number file path
#number_file_path = input("Please enter the path to the number file: ")
if not os.path.isfile(number_file_path):
    path = input("""Can not find the number file in input directory. Please make
sure you have a numbers.txt file in input directory and press enter
or enter your own path if the file is located somewhere else.

Enter alternate path or press enter to exit: """)
    if path == "":
        print("\nOperation stopped by USER : " + style.RED + "Could not find number file/altenate path not provided" + style.RESET)
        sys.exit()
    else:
        number_file_path = path
print(style.GREEN + "\nNumber file found." + style.RESET)


#image_path = input("Please enter the path to the image file: ")
ipath = ""
image = True
if not os.path.isfile(image_path):
    ipath = input("""Can not find the image file in input directory. If you want
to continue without an image, press enter or enter your own
path if the file is located somewhere else.

Enter alternate path or press enter to exit: """)
    image_path = ipath
    if ipath == "":
        print(style.RED + "\nNo image to be sent." + style.RESET)
        image = False
if image:
    print(style.GREEN + "\nImage file found." + style.RESET)

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
        if image_path != "":
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