import sys
from playwright.sync_api import sync_playwright

sys.path.append("..")
import config

class GitHubFetcher:
    BASE_URL = "https://api.github.com"

    def fetch_repo(self, owner: str, repo: str):
        with sync_playwright() as p:
            req = p.request.new_context()
            url = f"{self.BASE_URL}/repos/{owner}/{repo}"
            resp = req.get(url)
            data = resp.json()
            req.dispose()
            return data
