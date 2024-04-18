from selenium import webdriver 
from selenium.webdriver.common.by import By

# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# from selenium.webdriver.chrome.options import Options
  

search_string = "Four Seasons One Dalton Street"
search_string = search_string.replace(' ', '+')  
  
browser = webdriver.Chrome() 

for i in range(1): 
    matched_elements = browser.get("https://www.google.com/search?q=" +
                                     search_string + "&start=" + str(i))
    elements = browser.find_elements(By.TAG_NAME, 'a')
    # elt = browser.find_element(By.XPATH, "//div[@data-test-id='mainline-result-entity']")
    # elt = browser.find_element(By.CSS_SELECTOR, "div[class='result__info']")
    # elt = browser.find_element(By.CSS_SELECTOR, "a.result__source.result__source--ellipsis")
    # <a data-test-id="result-link" tabindex="-1" href="https://www.fourseasons.com/onedalton/" target="_self" rel="noopener" class="result__source result__source--ellipsis" data-v-88dc8ad8=""><span data-test-id="result-source" class="result__link" data-v-88dc8ad8=""><span class="source__content--domain" data-v-88dc8ad8="">https://www.fourseasons.com</span><span class="source__content--breadcrumbs" data-v-88dc8ad8=""> › onedalton
    #         </span></span></a>
    # elt = WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a [href]")))
    
for e in elements:
    print(e.text)

browser.quit()

# options = Options()
# options.add_argument('--ignore-certificate-errors')

# driver = webdriver.Chrome()
# driver.implicitly_wait(0.5)
# driver.get("https://www.canaryclubnyc.com/events")
# driver.find_element(By.CSS_SELECTOR, "input[class='text']").send_keys("testing")



