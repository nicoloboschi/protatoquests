import base64
import logging
import time
from functools import lru_cache

import requests

logger = logging.getLogger(__name__)

DEFAULT_CACHE_TTL = 300
cache_ttl_seconds = DEFAULT_CACHE_TTL

def set_cache_ttl(ttl: int):
    global cache_ttl_seconds
    cache_ttl_seconds = ttl

def get_cached_proxies():
    global cache_ttl_seconds
    cache_hash = round(time.time() / cache_ttl_seconds)
    return download_proxies(cache_hash=cache_hash)

@lru_cache
def download_proxies(cache_hash: int):
    response = requests.get("https://advanced.name/freeproxy?type=socks5")
    if response.status_code != 200:
        logger.error(f"Unable to scrape proxies: {response.status_code} {response.text})")
        return []
    from bs4 import BeautifulSoup
    parsed_html = BeautifulSoup(response.text)
    table = parsed_html.body.find("table", id="table_proxies")
    proxies = []
    for row in table.find_all("tr"):
        cols = row.find_all("td")
        if cols:
            ip = base64.b64decode(cols[1].get("data-ip")).decode("utf-8")
            port = base64.b64decode(cols[2].get("data-port")).decode("utf-8")
            proxies.append(f"{ip}:{port}")
    return proxies
