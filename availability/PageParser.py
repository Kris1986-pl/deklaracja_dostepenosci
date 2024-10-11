import re
import requests
from bs4 import BeautifulSoup

class PageParser:
    def __init__(self, url):
        self.url = url
        self.date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
        self.phone_number_pattern = re.compile(r'^47 \d{3} \d{2} \d{2}$')

    def get_elements_with_a11y_id(self):
        response = requests.get(self.url)
        elements = []

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            elements_with_a11y_id = soup.find_all(id=lambda x: x and "a11y" in x)

            for element in elements_with_a11y_id:
                element_id = element.get("id")
                element_text = element.text
                valid_format = None

                if "data" in element_id:
                    if self.date_pattern.match(element_text):
                        valid_format = "Poprawny format daty"
                    else:
                        valid_format = "Nieprawidłowy format daty. Powinnien być RRRR-MM-DD"
                elif "telefon" in element_id:
                    if self.phone_number_pattern.match(element_text):
                        valid_format = "Poprawny format numeru telefonu"
                    else:
                        valid_format = "Nieprawidłowy format numeru telefonu. Powinnien być 47 xxx xx xx"

                elements.append({"element_id": element_id, "element_text": element_text, "valid_format": valid_format})
        else:
            elements.append({"element_id": None, "element_text": "Nie udało się pobrać strony. Status code:", "valid_format": response.status_code})

        return elements