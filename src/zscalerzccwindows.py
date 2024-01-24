from common import dates, releasedata
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from datetime import date


product = releasedata.Product("zscalerzccwindows")
session = HTMLSession()
r = session.get('https://help.zscaler.com/eos-eol/supported-versions')
r.html.render(timeout=20)
#print(r.html.html)
session.close()

html_code = r.html.html

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_code, 'html.parser')

"""
# Select all <td> elements for software names and versions
software_data = soup.select("td:nth-child(2) , td:nth-child(1)")

# Iterate over pairs of software_name and software_version
for i in range(0, len(software_data), 2):
    software_name = software_data[i].get_text(strip=True)
    software_version = software_data[i + 1].get_text(strip=True)
    version = software_version
    date = date.today()
    #print(f"{software_name}: {software_version}")
    product.declare_version(version, date)
"""

# Parse the HTML using BeautifulSoup
#soup = BeautifulSoup(html_code, 'html.parser')

# Select all <td> elements for software names and versions
#software_data = soup.select(".table-responsive:nth-child(4) tr:nth-child(1) td:nth-child(2) , .table-responsive:nth-child(4) tr:nth-child(1) td:nth-child(1)")
software_data = soup.select("tr:nth-child(1) a")
# Iterate over pairs of software_name and software_version
for i in range(0, len(software_data), 2):
    software_1 = software_data[i].get_text(strip=True)
    software_2 = software_data[i + 1].get_text(strip=True)
    date = date.today()
    version = software_1
    product.declare_version(version, date)
    print(version + str(date))
    date = date.today()
    version = software_2
    product.declare_version(version, date)
    print(version + str(date))


product.write()
