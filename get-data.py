import asyncio
import aiohttp
import re
import requests


regular_for_phones = "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"

regular_for_phones = "([8,7]\d{3}\d{5})"

urls = [
    "https://hands.ru/company/about",
    # "https://repetitors.info",
]


async def async_fetch_page(session, url):
    async with session.get(url) as responnse:
        assert responnse.status == 200
        return await responnse.read()
    
    
def fetch_page(url):
    response = requests.get(url=url)
    assert response.status_code == 200
    return response.text


def handle_html(text):
    r = re.compile(regular_for_phones)
    match = r.findall(text)
    return match


if __name__ == "__main__":
    print("ok")
    loop = asyncio.get_event_loop()
    session = aiohttp.ClientSession(loop=loop)
    for url in urls:
        content = loop.run_until_complete(
            async_fetch_page(session, url)
        )
        content = content.decode()
        print(handle_html(content))
    session.close()
    loop.close()

