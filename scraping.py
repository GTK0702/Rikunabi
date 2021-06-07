from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
import openpyxl
import datetime

class Scraping:
    def __init__(self,url):
        self.url = url

    def gather(self,companies):
        coop_info = []
        for i in companies:
            coop_name = i

            options = webdriver.ChromeOptions()
            browser = webdriver.Chrome(ChromeDriverManager().install(),options=options)
            browser.get(self.url)
    
            search_coop=browser.find_element_by_id("mp_sp_input")
            search_coop.send_keys(coop_name)
            search_btn=browser.find_element_by_class_name("mp_input_submit")
            search_btn.click()
            coop = browser.find_element_by_class_name("ts-h-search-cassetteTitleMain").get_attribute("textContent")

            # 現在のハンドルを取得
            old_hdl = browser.window_handles[0]
            if coop_name in coop:
                coop_btn = browser.find_element_by_class_name("ts-h-search-cassetteTitleMain")
                coop_btn.click()
 
                # window_handlesで一覧を取得した後、old_hdlと一致しないものを探す。
                new_hdl = None
                for handle in browser.window_handles:
                    if new_hdl != handle:
                        new_hdl = handle
            
                # ウィンドウハンドルをnew_hdlに変更
                browser.switch_to_window(new_hdl)
                
                t = browser.find_element_by_id("company-data04").get_attribute("textContent")
                coop_info.append(t)
                print(t)
            browser.quit()

            #headlessモード    
            # options_headless = webdriver.ChromeOptions()
            # options_headless.add_argument('--headless')
            # browser_headless = webdriver.Chrome(ChromeDriverManager().install(),options=options_headless)
            # browser_headless.get(self.url)
    
            # search_coop=browser_headless.find_element_by_id("mp_sp_input")
            # search_coop.send_keys(coop_name)
            # search_btn=browser_headless.find_element_by_class_name("mp_input_submit")
            # search_btn.click()
            # coop = browser_headless.find_element_by_class_name("ts-h-search-cassetteTitleMain").get_attribute("textContent")
            # if coop_name in coop:
            #     coop_btn = browser_headless.find_element_by_class_name("ts-h-search-cassetteTitleMain")
            #     coop_btn.click()
                
            #     t = browser_headless.find_element_by_id("company-data04").get_attribute("textContent")
            #     coop_info.append(t)
            # browser_headless.quit()

        return coop_info

    def scr(self):
        t = browser_headless.find_element_by_id("company-data04").get_attribute("textContent")
        t.replace('\u3000', '')
        return t