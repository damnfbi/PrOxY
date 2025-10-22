import asyncio
import aiohttp
import json
import os
import sys
from datetime import datetime
from utils.proxy_scraper import ProxyScraper
from utils.validator import ProxyValidator
from utils.file_manager import FileManager

class ProxyMaster:
    def __init__(self):
        self.scraper = ProxyScraper()
        self.validator = ProxyValidator()
        self.file_manager = FileManager()
        
    async def run(self):
        print("starting proxy scraping session...")
        self.clear_terminal()
        

        print("scraping proxies from various sources...")
        raw_proxies = await self.scraper.scrape_all_sources()
        
        print(f"found {len(raw_proxies)} raw proxies")
        
        if not raw_proxies:
            print("no proxies found. check your internet connection.")
            return
            
        print("validating proxies (this will take ~30 seconds)...")
        

        validated_proxies = await self.validator.validate_proxies_with_progress(raw_proxies)
        

        self.file_manager.save_results(validated_proxies)
        

        self.display_summary(validated_proxies)
        
        return validated_proxies
    
    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_summary(self, proxies):
        good_count = len(proxies.get("good", []))
        bad_count = len(proxies.get("bad", []))
        unknown_count = len(proxies.get("unknown", []))
        total_count = good_count + bad_count + unknown_count
        
        print("\n" + "⎯⎯"*49)
        print("scraping session completed")
        print("⎯⎯"*49)
        print(f"good proxies - {good_count}")
        print(f"bad proxies - {bad_count}") 
        print(f"unknown proxies - {unknown_count}")
        print("⎯⎯"*49)
        
        if total_count > 0:
            success_rate = (good_count / total_count) * 100
            print(f"success rate - {success_rate:.1f}%")
        else:
            print(f"success rate - 0%")
            
        print("="*50)
        print(f"results saved in success/ directory")
        
        if good_count > 0:
            print(f"good proxies saved in success/good.json")
        print("="*50)

async def main():
    proxy_master = ProxyMaster()
    await proxy_master.run()

if __name__ == "__main__":
    asyncio.run(main())