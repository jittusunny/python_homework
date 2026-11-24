# Task 3
import json
import os

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


URL = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"


def build_driver():
    options = webdriver.ChromeOptions()
    options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


# Task 3 and Task 4
results = []

driver = None
try:
    # Durham County Library's robots.txt disallows all crawlers. This request is
    # intentionally not run as part of automated validation; the code remains
    # for educational use with the site's permission or if policy changes.
    raise RuntimeError(
        "Crawling Durham County Library is blocked by its robots.txt (User-agent: *; Disallow: /)."
    )

    driver = build_driver()
    driver.get(URL)
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li[data-test-id='searchResultItem']"))
    )

    # Repeating search-list entries and their nested fields.
    result_items = driver.find_elements(By.CSS_SELECTOR, "li[data-test-id='searchResultItem'].row")
    print("Search result count:", len(result_items))

    for item in result_items:
        title_elements = item.find_elements(By.CSS_SELECTOR, "h3.cp-title a, h3.cp-title, .title-content")
        title = title_elements[0].text.strip() if title_elements else ""

        author_elements = item.find_elements(By.CSS_SELECTOR, "a.cp-author-link, a.author-link")
        if not author_elements:
            author_elements = item.find_elements(By.CSS_SELECTOR, ".cp-author-link, .author-link")
        authors = ";".join(
            text for author in author_elements
            if (text := author.text.strip())
        )

        format_year = ""
        format_containers = item.find_elements(By.CSS_SELECTOR, ".manifestation-item-format-info-wrap")
        if not format_containers:
            format_containers = item.find_elements(By.CSS_SELECTOR, ".manifestation-item-format-call-wrap")
        if format_containers:
            spans = format_containers[0].find_elements(By.CSS_SELECTOR, "span")
            format_year = ";".join(span.text.strip() for span in spans if span.text.strip())

        results.append({
            "Title": title,
            "Author": authors,
            "Format-Year": format_year,
        })

    df = pd.DataFrame(results)
    print(df)

    assignment_directory = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(assignment_directory, "get_books.csv")
    json_path = os.path.join(assignment_directory, "get_books.json")

    df.to_csv(csv_path, index=False)
    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(results, json_file, indent=4)

except (TimeoutException, WebDriverException, NoSuchElementException) as error:
    print(f"A scraping error occurred: {type(error).__name__}: {error}")
except RuntimeError as error:
    print(error)
finally:
    if driver is not None:
        driver.quit()
