import aiohttp
import asyncio
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json

class ProxyScraper:
    def __init__(self):
        self.ua = UserAgent()
        self.timeout = aiohttp.ClientTimeout(total=10)
        
    async def fetch_url(self, session, url):
        try:
            headers = {'user-agent': self.ua.random}
            async with session.get(url, headers=headers, timeout=self.timeout) as response:
                return await response.text()
        except:
            return None
    
    async def scrape_all_sources(self):
        tasks = []
        async with aiohttp.ClientSession() as session:

            sources = [
                self.scrape_geonode(session),
                self.scrape_proxyscrape(session),
                self.scrape_proxyspace(session),
                self.scrape_freeproxyworld(session),
            ]
            
            results = await asyncio.gather(*sources, return_exceptions=True)
            
        all_proxies = set()
        for result in results:
            if isinstance(result, set):
                all_proxies.update(result)
                
        return list(all_proxies)
    
    async def scrape_geonode(self, session):
        proxies = set()
        try:
            url = "https://proxylist.geonode.com/api/proxy-list?limit=100&page=1&sort_by=lastChecked&sort_type=desc"
            content = await self.fetch_url(session, url)
            if content:
                data = json.loads(content)
                for proxy in data.get('data', []):
                    ip = proxy.get('ip')
                    port = proxy.get('port')
                    if ip and port:
                        proxies.add(f"{ip}:{port}")
        except:
            pass
        return proxies
    
    async def scrape_proxyscrape(self, session):
        proxies = set()
        try:
            url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=3000&country=all"
            content = await self.fetch_url(session, url)
            if content:
                for line in content.split('\n'):
                    line = line.strip()
                    if ':' in line and line.count('.') == 3:
                        proxies.add(line)
        except:
            pass
        return proxies
    
    async def scrape_proxyspace(self, session):
        proxies = set()
        try:
            url = "https://www.proxyspace.com/proxy/http"
            content = await self.fetch_url(session, url)
            if content:
                soup = BeautifulSoup(content, 'html.parser')

                for td in soup.find_all('td'):
                    text = td.text.strip()
                    if ':' in text and text.count('.') == 3:
                        proxies.add(text)
        except:
            pass
        return proxies
    
    async def scrape_freeproxyworld(self, session):
        proxies = set()
        try:
            url = "https://www.free-proxy-list.net/"
            content = await self.fetch_url(session, url)
            if content:
                soup = BeautifulSoup(content, 'html.parser')
                table = soup.find('table', {'class': 'table table-striped table-bordered'})
                if table:
                    for row in table.find_all('tr')[1:30]:
                        cols = row.find_all('td')
                        if len(cols) >= 2:
                            ip = cols[0].text.strip()
                            port = cols[1].text.strip()
                            if ip and port:
                                proxies.add(f"{ip}:{port}")
        except:
            pass
        return proxies