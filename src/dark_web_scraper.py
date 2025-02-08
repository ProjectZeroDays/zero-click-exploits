import aiohttp
import asyncio

class DarkWebScraper:
    async def fetch_data(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()

    async def scrape(self):
        urls = ['https://darkweb1.com', 'https://darkweb2.com']
        tasks = [self.fetch_data(url) for url in urls]
        return await asyncio.gather(*tasks)
