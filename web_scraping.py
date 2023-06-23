from bs4 import BeautifulSoup
import requests

url = "https://eyepax.com/job-openings/senior-software-engineer-php-react/"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
print(doc.prettify())