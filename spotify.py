from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

username = ""
password = ""


class Spotify:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome()

    def playMusic(self):
        self.browser.get("https://www.spotify.com/tr/")
        self.browser.maximize_window()
        first_Click = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/header/div/nav/ul/li[6]/a")));
        first_Click.click()

        second_Click = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/body/div[1]/div[2]/div/div[2]/div/a")));
        second_Click.click()

        Name = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.ID, "email")))
        Pass = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.ID, "pass")))
        Name.send_keys(self.username)
        Pass.send_keys(self.password)

        login_button = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.ID, "loginbutton")));
        login_button.click()

        Music = WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/footer/nav/div[2]/dl[3]/dd[2]/a")));
        Music.click()

        musicPlay = WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main']/div/div[4]/div[3]/footer/div/div[2]/div/div[1]/div[3]/button")));
        musicPlay.click()

        time.sleep(7)
        x, y = 998, 1019

        pyautogui.click(x, y)


spoti = Spotify(username, password)
spoti.playMusic()