# src/main.py
from pathlib import Path
import sys

# Add project root (one level above src/) to sys.path so root-level modules (config.py) can be imported
PROJECT_ROOT = str(Path(__file__).resolve().parents[1])
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Now safe to import root-level config
import config

from fetcher import Fetcher
from fetcher_github import GitHubFetcher
from transformer import transform_post, transform_todo
from transformer_github import transform_github_repo
from model import Unified
from utils.utils import write_ndjson

def main():
    
    # -------------------------
    # JSONPlaceholder data
    # -------------------------
    fetcher = Fetcher()
    posts = fetcher.fetch_posts()
    todos = fetcher.fetch_todos()

    # -------------------------
    # GitHub data
    # -------------------------
    github = GitHubFetcher()
    repo = github.fetch_repo("torvalds", "linux")  # Example repo

    # -------------------------
    # COMBINE ALL DATA
    # ------------------------

    def iter_unified():
        for p in posts:
            yield transform_post(p).model_dump()   # <- changed
        for t in todos:
            yield transform_todo(t).model_dump()   # <- changed
        # github repo
        yield transform_github_repo(repo).model_dump()


    count = write_ndjson(iter_unified(), config.OUTPUT_FILE)
    print(f"✔ Unified {count} items → {config.OUTPUT_FILE}")

if __name__ == "__main__":
    main()