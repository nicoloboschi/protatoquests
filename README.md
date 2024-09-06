# Protatoquests (Proxy Rotation Requests)

<p align="center">
  <a href="https://pypi.org/project/protatoquests/">
    <img src="https://img.shields.io/pypi/v/protatoquests?color=green&amp;label=pypi%20package" alt="PyPI">
  </a>
  <a href="https://pepy.tech/project/protatoquests">
    <img src="https://static.pepy.tech/badge/protatoquests" alt="Downloads">
  </a>
  <a href="">
    <img src="https://img.shields.io/pypi/pyversions/protatoquests?color=green" alt="Py versions">
  </a>
</p>
<hr>
<p align="center" style="font-size: 14px;">
Automatic proxy rotation for anonymous web requests.
</p>
<hr>

The intended usage is to by-pass server's IP blocking by using a pool of free proxies to perform requests and web scraping.
It's important to note that using anonymous proxies is **risky**, **unsafe** and will cause **credentials leaks**.

## Installation

```bash
pip install protatoquests
```

## Usage

```python
import requests
import protatoquests

# this one will contact the server directly
response = requests.get("https://google.com")
# this one will contact the server using an anonymous proxy 
response = protatoquests.get("https://google.com")
```

## Considerations

The library gets socks5 free proxies from [https://advanced.name/freeproxy](https://advanced.name/freeproxy).
It tries to use the first proxy available, if it fails, it tries the next one; therefore the **latency will be higher** than using a single proxy or no proxy at all.

## Contributing
Any contribution is welcome! Please open a PR with your changes.
