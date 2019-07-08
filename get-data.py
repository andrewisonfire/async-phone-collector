import asyncio
import aiohttp
import re
import requests
import time

regular_for_phones = "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"

regular_for_phones = "([8,7]\d{3}\d{5})"

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
    # "https://vk.com/flexbby",
    # "https://vk.com/griblee",
    # "https://vk.com/id1342733",
    # "https://vk.com/id72368811",
    # "https://vk.com/id72368811",
    # "https://vk.com/id72368812",
    # "https://vk.com/id72368813",
    # "https://vk.com/id72368814",
]

    
async def fetch_page(session, url):
    # async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
        response = await response.read()
        response = str(response)
        r = re.compile(regular_for_phones)
        match = r.findall(response)

        return match
        # return response


async def run(urls):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            task = asyncio.ensure_future(fetch_page(session, url))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        print(responses)

# async def handle_html(text):
#     r = re.compile(regular_for_phones)
#     match = await r.findall(text)
#     return match


def generate_urls(num):
    """"""
    for i in range(num):
        yield "https://vk.com/id{}".format(72368814+i)



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



    t1 = time.time()
    collector = PhoneCollector()

    for url in urls:
        content = collector.collect_data(url)

    print(collector.data)
    t2 = time.time()
    print(t2-t1)
    print("ok")
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(urls))
    loop.run_until_complete(future)
    print(time.time() - t2)




    # session = aiohttp.ClientSession(loop=loop)
    # for url in urls:
    #     content = loop.run_until_complete(
    #         async_fetch_page(session, url)
    #     )
    #     content = content.decode()
    #     print(handle_html(content))
    # session.close()
    # loop.close()

