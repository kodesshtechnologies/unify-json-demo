# src/fetcher.py
from playwright.sync_api import sync_playwright
from typing import Any, List
import sys
sys.path.append("..")  # to allow imports from root
import config

class Fetcher:
    def __init__(self, timeout: int = config.REQUEST_TIMEOUT_SECONDS):
        self.timeout = timeout

    def _get_json(self, url: str):
        with sync_playwright() as p:
            req = p.request.new_context()
            resp = req.get(url, timeout=self.timeout * 1000)
            data = resp.json()
            req.dispose()
            return data

    def fetch_posts(self) -> List[Any]:
        return self._get_json(config.POSTS_URL)

    def fetch_todos(self) -> List[Any]:
        return self._get_json(config.TODOS_URL)

