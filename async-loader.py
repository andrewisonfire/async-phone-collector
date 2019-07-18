import asyncio
import aiohttp
import re

# regular_for_phones =  "(?:\+7|8)(?:\d{2,3}){4}"
# #"([+]?[8,7]?[(]\d{3}?[}]\d{5})"
# "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"

re_1 = "([+]?[8,7][( ]?\d{3}[ )]?\d{3}[- ]?\d{2}[- ]?\d{2})"

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

class AsyncLoader:
    """

    """
    def __init__(self, regular_for_phones):
        self.regular_ex = re.compile(regular_for_phones)
        self.data = {}

    async def fetch_page(self, session, url):
        async with session.get(url) as response:
            if response.status == 200:
                response = await response.text()
                match = self.regular_ex.findall(response)
                return {
                    url: match
                }
            else:
                pass
    #         пометить url для повторного посещения

    async def run(self, urls):
        tasks = []
        async with aiohttp.ClientSession() as session:
            for url in urls:
                task = asyncio.ensure_future(self.fetch_page(session, url))
                tasks.append(task)

            responses = await asyncio.gather(*tasks)
            for response in responses:
                self.data.update(response)

    async def db_loader(self, phones):
        """
        put phones to database
        """


if __name__ == "__main__":
    loader = AsyncLoader(re_1)
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(loader.run(urls))
    loop.run_until_complete(future)
    print(loader.data)