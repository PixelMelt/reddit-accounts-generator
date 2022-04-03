
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from random import randint
import time 
import os



userNamePasswordFile = 'redditNameList.txt'
createdUserNamePasswordFile = 'createdNames.txt'


def create_account(username, password):
    #set up profile for proxy
    profile = webdriver.FirefoxProfile()
    browser = webdriver.Firefox(firefox_profile=profile)

    #get reddit account creation page
    browser.set_window_size(683, 744)
    browser.get('http://reddit.com/account/register/')
    #insert email
    time.sleep(randint(1,2))
    input("[*] Enter email, then press enter..." + '\n')
    #browser.find_element_by_id('regEmail').click()
    #browser.find_element_by_id('regEmail').send_keys("email@email.com")
    browser.find_element_by_css_selector('button.AnimatedForm__submitButton:nth-child(1)').click()
    time.sleep(randint(1,1))
    #insert username
    browser.find_element_by_id('regUsername').click()
    browser.find_element_by_id('regUsername').send_keys(username)
    #browser.find_element_by_css_selector('a.Onboarding__usernameSuggestion:nth-child(1)').click() #chooses the first random username
    #insert password
    time.sleep(randint(1,1))
    browser.find_element_by_id('regPassword').click()
    browser.find_element_by_id('regPassword').send_keys(password)
    #pause to manually enter captcha
    input('\n' + "[*] Solve captcha, create account, then press enter... enter 'r' as input if captcha doesn't appear to skip username" + '\n')
    if (input == 'r'):
        os.system('clear')
        browser.quit()
        return False
    else:
        browser.quit()
        return True





def main():
    os.system('clear')
    #run account generator for each user in list
    created = open(createdUserNamePasswordFile, 'a')
    creds = [cred.strip() for cred in open(userNamePasswordFile).readlines()]
    for cred in creds:
        username, password = cred.split(':')
        print('[+] creating account for %s with password %s' % (username,password))
        account_created = create_account(username, password)
        print('[+] ')
        input('\n' + "[*] get a new ip address, then press enter..." + '\n')
        #os.system('service tor restart')
        if account_created:
            print('[+] writing name:password to created names...')
            created.write(username + ':' + password + '\n')
            print('[+] deleting name:password from original file...')
            lines = [line.strip() for line in open(userNamePasswordFile).readlines()]
            f = open(userNamePasswordFile, 'w')
            for line in lines:
                if (line != cred):
                    f.write(line + "\n")
            f.close()
        else:
            print('[-] name not recorded due to captcha issue')
        time.sleep(2)
        os.system('clear')
    created.close()

    
main()
