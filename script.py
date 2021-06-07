import openpyxl
import datetime

from excel import Excel
from scraping import Scraping

excel = Excel()
companies = excel.companies_name()

url = "https://job.rikunabi.com/2022/"
scraping = Scraping(url)
scraping = scraping.gather(companies)

print(scraping)

