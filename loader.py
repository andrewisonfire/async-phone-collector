import re
import time
import requests

regular_for_phones = "([+]?[8,7]\d{3}\d{5})"
# test = "^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$"

urls = [
    "https://hands.ru/company/about",
    "https://repetitors.info",
    "https://hands.ru/company/about",
    "https://repetitors.info",
    "https://hands.ru/company/about",
    "https://repetitors.info",
    "https://hands.ru/company/about",
    "https://repetitors.info",
    "https://hands.ru/company/about",
    "https://repetitors.info",
    "https://hands.ru/company/about",
    "https://repetitors.info",
]


async def fetch_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()


class PhoneCollector:

    def __init__(self):
        self.data = {}

    def fetch_page(self, url):
        response = requests.get(url=url)
        assert response.status_code == 200
        return response.text

    def handle_html(self, text):
        r = re.compile(regular_for_phones)
        match = r.findall(text)
        return match

    def collect_data(self, url):
        self.data.setdefault(url,
            self.handle_html(self.fetch_page(url))
        )

    def validate_data(self):
        """
        :yield: phone number to validator
        """
        pass

if __name__ == "__main__":

    collector = PhoneCollector()
    t1 = time.time()
    for url in urls:
        content = collector.collect_data(url)

    print(collector.data)
    print(time.time()-t1)
