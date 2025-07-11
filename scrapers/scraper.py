# scrapers/scraper.py
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


def ias_scraper(url):
    print("Running ias belgium scraper")
    HEADLESS = True
    firefox_options = Options()

    if HEADLESS:
        firefox_options.add_argument("--headless")

    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=firefox_options)
    driver.get(url)
    time.sleep(4)  # Wait for the page to load
    elem = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//table[@class="invasive"]//tr[td/a]'))
    )  # This is a dummy element)
    # Find the number of invasive alien species currently listed by Belgium.
    elem = driver.find_element(By.XPATH, '//p[contains(text(), "Harmonia includes")]/span')
    print(elem.text)

    # Find all of these invasive species names, both scientific and common, and store them in a dict (key: latin name, value: common name).
    species_dict = {}

    # sci_name_elements = driver.find_elements(By.XPATH, '//table[@class="invasive"]//tr/td/a')

    rows = driver.find_elements(By.XPATH, '//table[@class="invasive"]//tr[td/a]')
    for row in rows:
        try:
            sci_elem = row.find_element(By.XPATH, ".//td/a")
            sci_name = sci_elem.text.strip()

            common_name_td = sci_elem.find_element(By.XPATH, "./ancestor::td[1]/following-sibling::td[1]")
            common_name = common_name_td.text.strip()

            species_dict[sci_name] = common_name
        except Exception:
            continue

    print(f"Found {len(species_dict)} species")
    print(species_dict)
    print(len(species_dict))
    # for latin, common in species_dict.items():
    #     print(f"{latin} — {common}")

    if driver:
        driver.quit()
    print("Done scraping, webdriver closed. Exiting now.")
    return species_dict


def csv_writer(species_dict, file):
    print("Writing to CSV")
    species_df = pd.DataFrame(list(species_dict.items()), columns=["Scientific Name", "Common Name"])
    species_df["Common Name"] = species_df["Common Name"].str.replace('"', "", regex=False)
    print(species_df)
    species_df.to_csv("ias_species.csv", index=False)
    # with open("ias_belgium_species.csv", "w", newline="", encoding="utf-8") as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerow(["Latin Name", "Common Name"])
    #     for latin_name, common_name in species_dict.items():
    #         writer.writerow([latin_name, common_name])
    # print("CSV writing complete.")


# The handler function gets called by the dockerfile.
def handler(event, context):
    print("running Handler")
    # starttime = time.time()
    # file = "ias_belgium_species.csv"
    # ias_url = "https://ias.biodiversity.be/species/all"
    # species_dict = ias_scraper(ias_url)
    # csv_writer(species_dict, file)
    # endtime = time.time()
    # print(f"Execution time: {endtime - starttime} seconds")


# This is for testing locally; the handler function will be called by AWS Lambda.
if __name__ == "__main__":
    handler(None, None)
