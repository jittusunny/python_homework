# Task 6
import csv
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


URL = "https://top10.owasp.org/2021/"

options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options,
)

try:
    driver.get(URL)

    top_10 = []
    seen_urls = set()

    # XPath selects OWASP Top 10 2021 entry links, not every navigation link.
    vulnerability_links = driver.find_elements(
        By.XPATH,
        "//a[contains(@href, 'A01_2021') or contains(@href, 'A02_2021') or contains(@href, 'A03_2021') or contains(@href, 'A04_2021') or contains(@href, 'A05_2021') or contains(@href, 'A06_2021') or contains(@href, 'A07_2021') or contains(@href, 'A08_2021') or contains(@href, 'A09_2021') or contains(@href, 'A10_2021')]",
    )

    for link in vulnerability_links:
        title = link.text.strip()
        href = link.get_attribute("href")
        if title and href and href not in seen_urls:
            top_10.append({"title": title, "href": href})
            seen_urls.add(href)

    top_10.sort(key=lambda item: item["title"][:3])
    print(top_10)

    assignment_directory = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(assignment_directory, "owasp_top_10.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["title", "link"])
        writer.writeheader()
        for item in top_10:
            writer.writerow({"title": item["title"], "link": item["href"]})

finally:
    driver.quit()
