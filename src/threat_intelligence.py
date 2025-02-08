import aiohttp
import asyncio

class ThreatIntelligence:
    def __init__(self):
        self.sources = [
            "https://api.threatsource1.com/v1/threats",
            "https://api.threatsource2.com/v1/threats",
            "https://api.threatsource3.com/v1/threats"
        ]

    async def fetch_data(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()

    async def fetch_all_data(self):
        tasks = [self.fetch_data(url) for url in self.sources]
        return await asyncio.gather(*tasks)

    def process_data(self, data):
        # Placeholder for data processing logic
        processed_data = []
        for source_data in data:
            for threat in source_data:
                processed_data.append({
                    "threat_id": threat["id"],
                    "description": threat["description"],
                    "severity": threat["severity"],
                    "timestamp": threat["timestamp"]
                })
        return processed_data

    async def get_threat_intelligence(self):
        raw_data = await self.fetch_all_data()
        return self.process_data(raw_data)
