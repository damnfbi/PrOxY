import json
import os
from datetime import datetime

class FileManager:
    def __init__(self):
        self.ensure_directories()
    
    def ensure_directories(self):
        os.makedirs("success", exist_ok=True)
        os.makedirs("utils", exist_ok=True)
    
    def save_results(self, proxies):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        

        if proxies["good"]:
            good_file = f"success/good_{timestamp}.json"
            with open(good_file, 'w') as f:
                json.dump({
                    "metadata": {
                        "total_proxies": len(proxies["good"]),
                        "scraped_at": datetime.now().isoformat(),
                        "type": "residential"
                    },
                    "proxies": proxies["good"]
                }, f, indent=2)
            

            with open("success/good.json", 'w') as f:
                json.dump(proxies["good"], f, indent=2)
        

        if proxies["bad"]:
            bad_file = f"success/blyat_{timestamp}.json"
            with open(bad_file, 'w') as f:
                json.dump(proxies["bad"], f, indent=2)
            
            with open("success/blyat.json", 'w') as f:
                json.dump(proxies["bad"], f, indent=2)
        

        if proxies["unknown"]:
            unknown_file = f"success/unknown_{timestamp}.json"
            with open(unknown_file, 'w') as f:
                json.dump(proxies["unknown"], f, indent=2)
            
            with open("success/unknown.json", 'w') as f:
                json.dump(proxies["unknown"], f, indent=2)