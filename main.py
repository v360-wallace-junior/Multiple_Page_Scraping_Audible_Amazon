from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

WEB_URL = 'https://www.audible.com.br/search'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument("--headless=new")
# chrome_options.add_argument("--window-size=1920,1080")
# chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

# # Evita o bloqueio desativando as flags de automação
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_experimental_option('useAutomationExtension', False)

# # Argumentos cruciais para rodar em ambientes Linux (como o seu caminho /home/wallace-junior-360/)
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")


driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#     "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
# })

try:
    driver.get(WEB_URL)

    espera = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "adbl-impression-container"))
    )

    # Paginacao
    pagination = driver.find_element(By.XPATH, '//ul[contains(@class, "pagingElements")]')
    pages = pagination.find_elements(By.XPATH, './li')
    last_page = int(pages[-2].text)
    current_page = 1

    book_title = []
    book_author = []
    book_length = []

    while current_page <= last_page:

        container = driver.find_element(By.CLASS_NAME, 'adbl-impression-container')
        products = container.find_elements(By.XPATH, './div/span/ul/li')

        for product in products:
            book_title.append(product.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]').text)
            book_author.append(product.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]').text)
            book_length.append(product.find_element(By.XPATH, './/li[contains(@class, "runtimeLabel")]').text)

        current_page+=1

        try:
            next_page = driver.find_element(By.XPATH, '//span[contains(@class, "nextButton")]')
            next_page.click()
        except Exception as e:
            print(f'Erro de paginacao: {e}')

    df_book = pd.DataFrame({ 'title': book_title, 'author': book_author, 'length': book_length })
    df_book.to_csv('books.csv', index=False)

finally:
    driver.quit()