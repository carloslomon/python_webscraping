from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    # Set up Selenium WebDriver
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/@AsambleaCRC/videos")
    
    # Wait for the page to load and content to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.ID, "video-title"))
    )
    
    # Find video titles and views
    titles = driver.find_elements(By.ID, "video-title-link")
    views = driver.find_elements(By.XPATH, "//span[contains(@class, 'inline-metadata-item') and contains(text(), 'views')]")
    
    # Print video titles and views
    for title, view in zip(titles, views):
        print(f"Title: {title.text} - Views: {view.text}")
    
    # Close the driver
    driver.quit()

main()
