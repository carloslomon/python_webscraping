from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def find_views(label):
    """Extracts the number of views from the aria-label text."""
    words = label.lower().split(" ")
    for i, word in enumerate(words):
        if word == "views":
            if words[i-1].replace(',', '').isdigit():  # Handle comma in numbers
                return words[i-1]
            elif i > 1 and words[i-2].replace(',', '').isdigit():
                return f"{words[i-2]} {words[i-1]}"
    return "Unknown"

def main():
    # Set up Selenium WebDriver
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/@AsambleaCRC/videos")

    try:
        # Wait for video elements to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.ID, "video-title-link"))
        )

        # Get page source and parse with BeautifulSoup
        content = driver.page_source
        soup = BeautifulSoup(content, 'lxml')

        # Find video titles and aria-labels
        video_links = soup.find_all('a', id="video-title-link")

        for video in video_links:
            title = video['title'] if 'title' in video.attrs else "No Title"
            aria_label = video['aria-label'] if 'aria-label' in video.attrs else "No Aria Label"
            href = video['href'] if 'href' in video.attrs else "No Link"
            views = find_views(aria_label)
            
            print(f"Title: {title}")
            print(f"Views: {views}")
            print(f"Link: https://www.youtube.com{href}\n")

    finally:
        # Close the driver
        driver.quit()

if __name__ == "__main__":
    main()
