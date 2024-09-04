# `requests-anon`

Execute HTTPS requests to a server using anonymous proxies.
The intended usage is to by-pass server's IP Blocking while scraping data from API or webpages.
It's important to note that using anonymous proxies is **risky**, **unsafe** and will cause **credentials leaks**.

## Installation

```bash
pip install requests-anon
```

## Usage

```python
import requests
from requests_anon import request_with_anon_proxy_unsafe

# this one will contact the server directly
response = requests.get("https://google.com")
# this one will contact the server using an anonymous proxy 
response = request_with_anon_proxy_unsafe("get", "https://google.com")
```

## Considerations

The library gets socks5 free proxies from [https://advanced.name/freeproxy](https://advanced.name/freeproxy).
It tries to use the first proxy available, if it fails, it tries the next one; therefore the **latency will be higher** than using a single proxy or no proxy at all.

## Contributing
Any contribution is welcome! Please open a PR with your changes.