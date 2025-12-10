import requests
from bs4 import BeautifulSoup

req = requests.get("https://divar.ir/s/shiraz/motorcycles")
soup = BeautifulSoup(req.text, "html.parser")
variable = soup.find_all(class_="kt-post-card__body")
for i in variable:
    if "توافق" in i.text:
        print(i.tex)
    if "توافقی" in i.text:
        print(i.tex)
