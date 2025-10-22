```markdown
# PrOxY

> **advanced residential proxy scraping suite**  
> *clean, fast, and reliable proxy acquisition tool*

---

## 📁 project structure

```
PrOxY/
├── main.py                 # primary execution file
├── requirements.txt        # dependencies
├── run_fixed.py           # testing script
├── quick_test.py          # rapid validation script
├── success/               # output directory
│   ├── good.json         # verified working proxies
│   ├── blyat.json        # failed/invalid proxies  
│   └── unknown.json      # unclassified proxies
└── utils/                 # core modules
    ├── proxy_scraper.py  # multi-source proxy extraction
    ├── validator.py      # proxy validation & testing
    └── file_manager.py   # results management
```

---

## 🚀 quick start

### installation
```bash
# clone and setup
git clone <repository-url>
cd PrOxY

# install dependencies
pip install -r requirements.txt

# run the tool
python main.py
```

### rapid testing
```bash
# quick validation (15 proxies)
python quick_test.py

# verified fixed version
python run_fixed.py
```

---

## ⚡ features

- **multi-source scraping** - aggregates proxies from 4+ reliable sources
- **async validation** - concurrent testing for maximum speed
- **real-time progress** - visual progress tracking during validation
- **clean json output** - structured results for easy integration
- **cross-platform** - works on windows/linux/macos
- **error resilient** - continues operation despite failures
- **auto-organization** - categorizes proxies by status

---

## 🔧 core components

### `proxy_scraper.py`
- geonode api integration
- proxyscrape api access  
- free-proxy-list parsing
- proxy-space extraction
- duplicate prevention

### `validator.py`
- multi-endpoint testing (httpbin, ipify, ipinfo)
- response time measurement
- concurrent connection management
- automatic retry logic

### `file_manager.py`
- timestamped backup files
- json formatting
- directory management
- results categorization

---

## 📊 output format

### good.json
```json
{
  "proxy": "192.168.1.1:8080",
  "status": "good",
  "type": "residential",
  "response_time": "245ms",
  "test_url": "http://httpbin.org/ip",
  "validated_at": "2024-01-15t10:30:00.000000"
}
```

### session summary
```
==================================================
scraping session completed
==================================================
good proxies - 29
bad proxies - 19
unknown proxies - 301
==================================================
success rate - 8.3%
==================================================
```

---

## 🛠️ dependencies

```txt
requests==2.31.0
beautifulsoup4==4.12.2
aiohttp==3.8.5
asyncio==3.4.3
fake-useragent==1.4.0
colorama==0.4.6
```

---

## 🎯 usage examples

### basic scraping
```python
from utils.proxy_scraper import ProxyScraper

scraper = ProxyScraper()
proxies = await scraper.scrape_all_sources()
```

### proxy validation  
```python
from utils.validator import ProxyValidator

validator = ProxyValidator()
results = await validator.validate_proxies_with_progress(proxies)
```

### integration
```python
from main import ProxyMaster

proxy_master = ProxyMaster()
results = await proxy_master.run()
```

---

## 📈 performance

- **scraping speed**: 5-10 seconds for 300+ proxies
- **validation speed**: 20-30 seconds for 500 proxies  
- **success rate**: 5-15% (typical for free proxies)
- **concurrency**: 15 simultaneous connections
- **timeout**: 2 seconds per proxy test

---

## 🔄 workflow

1. **initialization** - clear terminal, setup directories
2. **scraping phase** - extract proxies from multiple sources
3. **validation phase** - test proxies with progress tracking
4. **categorization** - sort into good/bad/unknown
5. **output generation** - save results with metadata
6. **summary display** - show statistics and success rates

---

## 📞 support

**developer**: [damnfbi](https://t.me/damnfbi)  
**issues**: please include error logs and system information

---

## ⚠️ disclaimer

for educational and development purposes only.  
respect api rate limits and website terms of service.  
users are responsible for compliant usage.

---

## 🎨 aesthetic notes

- clean lowercase text throughout
- consistent symbol usage (no colons in output)
- progress visualization
- structured json responses
- cross-platform terminal compatibility

```

*built with attention to detail for developers who value clean code and reliable tools* 🛠️