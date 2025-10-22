import aiohttp
import asyncio
from datetime import datetime
import time

class ProxyValidator:
    def __init__(self):
        self.test_urls = [
            "http://httpbin.org/ip",
            "http://api.ipify.org?format=json", 
            "http://ipinfo.io/json"
        ]
        self.timeout = aiohttp.ClientTimeout(total=2)  
        self.semaphore = asyncio.Semaphore(15)  
        
    async def validate_proxy(self, proxy):
        for test_url in self.test_urls:
            try:
                proxy_url = f"http://{proxy}"
                
                async with self.semaphore:
                    connector = aiohttp.TCPConnector(verify_ssl=False)
                    async with aiohttp.ClientSession(connector=connector, timeout=self.timeout) as session:
                        start_time = time.time()
                        async with session.get(test_url, proxy=proxy_url) as response:
                            if response.status == 200:
                                data = await response.json()
                                response_time = (time.time() - start_time) * 1000
                                
                                return {
                                    "proxy": proxy,
                                    "status": "good",
                                    "type": "residential", 
                                    "response_time": f"{response_time:.0f}ms",
                                    "test_url": test_url,
                                    "validated_at": datetime.now().isoformat()
                                }
            except asyncio.TimeoutError:
                continue  
            except Exception as e:
                continue  
        
        return {"proxy": proxy, "status": "bad", "error": "all tests failed"}
    
    async def validate_proxies_with_progress(self, proxies):
        total = len(proxies)
        if total == 0:
            return {"good": [], "bad": [], "unknown": []}
            
        completed = 0
        good_proxies = []
        bad_proxies = []
        
        print(f"validating {total} proxies...")
        print("progress: [", end="", flush=True)
        
        batch_size = 20
        batches = [proxies[i:i + batch_size] for i in range(0, total, batch_size)]
        
        for i, batch in enumerate(batches):
            tasks = [self.validate_proxy(proxy) for proxy in batch]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            for result in results:
                if isinstance(result, dict):
                    if result.get("status") == "good":
                        good_proxies.append(result)
                    else:
                        bad_proxies.append(result)
            
            completed += len(batch)
            progress_percent = (completed / total) * 100
            bars = int((completed / total) * 50)
            print("#" * (bars - (i * 10)), end="", flush=True)
        
        print("] 100%")
        
        return {
            "good": good_proxies,
            "bad": bad_proxies,
            "unknown": []
        }