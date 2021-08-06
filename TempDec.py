#!/usr/bin/env python3

import sys, os, traceback
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, random
from datetime import datetime as dt
from pytz import timezone


class TempDecl:
    driver = None

    def __init__(self):
        custom_options = webdriver.ChromeOptions()
        custom_options.add_argument('--no-sandbox')
        custom_options.add_argument("--disable-gpu")
        custom_options.add_argument('--headless')
        custom_options.add_argument("--incognito")
        custom_options.add_argument("--window-size=800,600")
        custom_options.add_argument("--disable-blink-features=AutomationControlled")
        

        self.tz = timezone('Asia/Singapore')
        self.driver = webdriver.Chrome(options=custom_options)
        self.driver.get("https://myaces.nus.edu.sg/htd")


    def login(self):
        try:
            load_dotenv()
            userid = os.environ["USERID"]
            pwd = os.environ["PASSWORD"]

            userName = self.driver.find_element_by_id("userNameInput")
            userName.send_keys(userid)

            password = self.driver.find_element_by_id("passwordInput")
            password.send_keys(pwd)

            submitButton = self.driver.find_element_by_id("submitButton")
            submitButton.click()

            print("Logged in")

            time.sleep(0.2)

        except:
            traceback.print_exc()
            exit()


    def selectAm(self):
        try:
            amPmDropdown = Select(self.driver.find_element_by_name("declFrequency"))
            amPmDropdown.select_by_index(0)

            time.sleep(0.2)

        except:
            print("AM/PM option not found!")


    def selectPm(self):
        try:
            amPmDropdown = Select(self.driver.find_element_by_name("declFrequency"))
            amPmDropdown.select_by_index(1)

            time.sleep(0.2)

        except:
            print("AM/PM option not found!")


    def declTemp(self, am: bool = True):
        try:
            symptomsButton = WebDriverWait(self.driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='radio'][name='symptomsFlag'][value='N']"))
            )
            symptomsButton.click()

            time.sleep(0.2)

            houseHoldButton = self.driver.find_element_by_css_selector("input[type='radio'][name='familySymptomsFlag'][value='N']")
            houseHoldButton.click()

            time.sleep(0.2)

            if am: self.selectAm()

            tempInput = self.driver.find_element_by_id("temperature")
            temp = ("{:.1f}".format(random.uniform(35.6, 36.5)))
            tempInput.send_keys(temp)

            time.sleep(0.2)

            submitButton = self.driver.find_element_by_name("Save")
            submitButton.click()

            time.sleep(0.2)
            print("Declared {} temperature at {}!".format("am" if am else "pm", dt.now(self.tz)))

        except:
            traceback.print_exc()

        finally:
            time.sleep(0.2)
            self.driver.quit()

def declareAmTemp():
    AM = TempDecl()
    AM.login()
    AM.declTemp(am=True)

def declarePmTemp():
    PM = TempDecl()
    PM.login()
    PM.declTemp(am=False)


def main():
    declareAm = False
    declarePm = False

    if "-am" in sys.argv:
        declareAm = True
    if "-pm" in sys.argv:
        declarePm = True

    if (declareAm):
        declareAmTemp()

    if (declarePm):
        declarePmTemp()

    if (not declareAm and not declarePm):
        tz =  timezone('Asia/Singapore')
        now = dt.now(tz)
        hour = now.hour

        if hour < 12:
            declareAmTemp()
    
        if hour >= 12:
            declarePmTemp()

main()
