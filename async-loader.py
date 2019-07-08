import asyncio
import aiohttp
import time
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
    не совсем то
    надо сделать что-то типа очереди
    которая асинхронно читает из базы и отдаёт в загрузчик url'ы
    """
    @staticmethod
    async def fetch_page(session, url):
        # async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            response = str(response)
            r = re.compile(regular_for_phones)
            match = r.findall(response)

            return match
            # return response

    @staticmethod
    async def run(urls):
        tasks = []
        async with aiohttp.ClientSession() as session:
            for url in urls:
                task = asyncio.ensure_future(AsyncLoader.fetch_page(session, url))
                tasks.append(task)

            responses = await asyncio.gather(*tasks)
            print(responses)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(AsyncLoader.run(urls))
    loop.run_until_complete(future)