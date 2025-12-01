# config.py
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

POSTS_URL = os.getenv("POSTS_URL", "https://jsonplaceholder.typicode.com/posts")
TODOS_URL = os.getenv("TODOS_URL", "https://jsonplaceholder.typicode.com/todos")

OUTPUT_FILE = Path(os.getenv("OUTPUT_FILE", "output/unified.ndjson"))

REQUEST_TIMEOUT_SECONDS = int(os.getenv("REQUEST_TIMEOUT_SECONDS", "30"))
