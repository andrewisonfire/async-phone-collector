import asyncio
import aiohttp
import re

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
]

class AsyncLoader:
    """

    """
    def __init__(self, regular_for_phones):
        self.regular_ex = re.compile(regular_for_phones)

    async def fetch_page(self, session, url):
        async with session.get(url) as response:
            if response.status == 200:
                response = await response.text()
                match = self.regular_ex.findall(response)
                return match

    async def run(self, urls):
        tasks = []
        async with aiohttp.ClientSession() as session:
            for url in urls:
                task = asyncio.ensure_future(self.fetch_page(session, url))
                tasks.append(task)

            responses = await asyncio.gather(*tasks)
            print(responses)


if __name__ == "__main__":
    loader = AsyncLoader(regular_for_phones)
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(loader.run(urls))
    loop.run_until_complete(future)
