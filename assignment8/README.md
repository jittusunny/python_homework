# Assignment 8: Introduction to Web Scraping

## Task 1 — Durham County Library robots.txt compliance

The Durham County Library robots.txt file is:

- `User-agent: *`
- `Disallow: /`

It also disallows `/` for `Yandex` and `YandexBot`. Therefore, automated crawling of the search URL is not permitted. The educational scraper is written but deliberately stops before making a Durham request. No live Durham scraping was performed.

## Task 2 — DOM/selector notes

The repeating search-result container is an `li` with `data-test-id="searchResultItem"` and class `row cp-search-result-item`.

Useful nested selectors:

- Title: `h3.cp-title`, `h3.cp-title a`, or `.title-content`
- Author: `a.cp-author-link`, `a.author-link`, `.cp-author-link`, or `.author-link`
- Format/container: `.manifestation-item-format-info-wrap`, `.manifestation-item-format-call-wrap`, or the containing `div`

Selectors can change, so the program catches missing fields instead of assuming every result has the same structure.

## Task 5 — Wikipedia robots.txt

See `ethical_scraping.txt`.

## Task 6 — OWASP

See `owasp_top_10.py`. The script uses XPath to find the ten vulnerability links on the OWASP 2021 Top Ten page and writes `owasp_top_10.csv`.

## Running

```bash
cd python_homework
python -m pip install selenium webdriver-manager pandas
python assignment8/owasp_top_10.py
python assignment8/get_books.py
```