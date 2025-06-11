from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializa o navegador
driver = webdriver.Chrome()

try:
    # 1. Acessa o site
    driver.get("https://books.toscrape.com/")
    print("1. Acessou a página inicial")
    time.sleep(2)

    # 2. Clica na categoria "Travel"
    travel_link = driver.find_element(By.LINK_TEXT, "Travel")
    travel_link.click()
    print("2. Clicou na categoria Travel")
    time.sleep(2)

    # 3. Clica no primeiro livro listado
    first_book = driver.find_element(By.CSS_SELECTOR, "h3 a")
    first_book.click()
    print("3. Clicou no primeiro livro da categoria")
    time.sleep(2)

    # 4. Volta para a página anterior
    driver.back()
    print("4. Voltou para a página da categoria")
    time.sleep(2)

    # 5. Vai para a home novamente
    home_link = driver.find_element(By.LINK_TEXT, "Books to Scrape")
    home_link.click()
    print("5. Voltou para a home")
    time.sleep(2)

    # 6. Salva o HTML da página atual
    page_source = driver.page_source
    with open("pagina_books.html", "w", encoding="utf-8") as f:
        f.write(page_source)
    print("✅ HTML da home salvo como 'pagina_books.html'")

finally:
    driver.quit()
    print("🚀 Teste finalizado com sucesso.")
