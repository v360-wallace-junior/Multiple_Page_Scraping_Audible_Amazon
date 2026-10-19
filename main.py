from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

WEB_URL = 'https://www.audible.com.br/search'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get(WEB_URL)

    espera = WebDriverWait(driver, 10)

    titulo = espera.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "adbl-impression-container"))
    )

    container = driver.find_element(By.CLASS_NAME, 'adbl-impression-container')
    products = container.find_elements(By.XPATH, './div/span/ul/li')

    book_title = []
    book_author = []
    book_length = []


    for product in products:
        # print(product.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]').text)
        book_title.append(product.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]').text)
        book_author.append(product.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]').text)
        book_length.append(product.find_element(By.XPATH, './/li[contains(@class, "runtimeLabel")]').text)

    
    df_book = pd.DataFrame({ 'title': book_title, 'author': book_author, 'length': book_length })
    df_book.to_csv('books.csv', index=False)
finally:
    driver.quit()