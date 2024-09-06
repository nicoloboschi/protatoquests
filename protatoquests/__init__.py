import requests
import logging

from protatoquests.proxy import download_proxies, get_cached_proxies

logger = logging.getLogger(__name__)

def get(url, **kwargs):
    return request("GET", url, **kwargs)


def post(url, **kwargs):
    return request("POST", url, **kwargs)

def put(url, **kwargs):
    return request("PUT", url, **kwargs)


def delete(url, **kwargs):
    return request("DELETE", url, **kwargs)


def patch(url, **kwargs):
    return request("PATCH", url, **kwargs)


def request(method, url, **kwargs):
    return _request_with_proxy(False, method, url, **kwargs)


def _request_with_proxy(ssl_verify, method, url, **kwargs):
    proxies = get_cached_proxies()
    for proxy in proxies:
        logger.debug(f"Using proxy: {proxy}")
        try:
            args = {**kwargs, "proxies": {"https": "socks5://" + proxy}}
            if not ssl_verify:
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

    logger.warning("Failed to execute request with proxies, falling back to not using proxy")
    return requests.request(method, url, **kwargs)
