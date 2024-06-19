import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cosmed:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("chrome://settings/")
        driver.execute_script("chrome.settingsPrivate.setDefaultZoom(0.8)")
        driver.get("https://shop.cosmed.com.tw/")
        self.driver = driver

    def check_cookie_dialog(self):
        # close cookie dialog
        cookie_notice = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'cookie')]")
            )
        )

        if cookie_notice is None:
            print("not find cookie notice")
            return
        
        print("find cookie notice, continue find close button")
        i_know_button = cookie_notice.find_element(
            By.XPATH, "//a[contains(text(), '我知道了')]"
        )

        if i_know_button is None:
            print("not find close cookie button")
            return
        
        i_know_button.click()
        print("i_know_button clicked")

    def check_ads(self):
        # close ads
        ads_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//img[contains(@alt, 'Ads')]"))
        )

        if ads_element is None:
            print("not find ads")
            return
        
        print("find ads, continue find close button")
        closeBtn = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '✕')]"))
        )

        if closeBtn is None:
            print("not find close ads button")
            return
        
        closeBtn.click()
        print("close ads button clicked")

    def enter_search_key(self, search_key):
        # start search
        search_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ns-search-input"))
        )
        search_text.send_keys(search_key)
        search_text.send_keys(webdriver.Keys.RETURN)
        print("search key => ",search_key)

    def add_first_item_to_cart(self):
        # check search item
        items = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "column-grid-container__column")
            )
        )

        if items[0] is None:
            print("search first item is null")
            return
        
        items[0].click()
        print("search first item clicked")
        
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "add-to-cart-btn")))
    

        if add_to_cart_button is None:
            print("cart_button is not find")
            return
    
        add_to_cart_button.click()
        print("add_to_cart_button clicked")
        
    def get_current_cart_num(self) -> int:
        time.sleep(2)
        badge_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(@class, 'round-badge cms-badge')]")
            )
        )
        badge_text = badge_element.text
        print("badge = ", badge_text)
        self.driver.quit()
        return int(badge_text)
    
    def quit_chrome(self):
        self.driver.quit()