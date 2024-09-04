import logging
import requests
logger = logging.getLogger(__name__)


def anon_request(method, url, **kwargs):
    return _request_with_proxy(False, method, url, **kwargs)


def _request_with_proxy(safe, method, url, **kwargs):
    response = requests.get("https://advanced.name/freeproxy/66d817afbff12?type=socks5")
    response.raise_for_status()
    proxies = response.text.splitlines()
    for proxy in proxies:
        logger.debug(f"Testing proxy {proxy}")
        try:
            args = {**kwargs, "proxies": {"https": "socks5://" + proxy}}
            if not safe:
                args["verify"] = False
            response = requests.request(method, url, **args)
        except Exception as e:
            logger.debug(f"Proxy {proxy} failed: {e}")
            continue
        if response.status_code < 400:
            logger.debug(f"Proxy {proxy} success")
            return response
        else:
            logger.debug(f"Proxy {proxy} failed: {response.status_code}: {response.text}")
