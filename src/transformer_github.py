from datetime import datetime
from model import Unified

def transform_github_repo(item: dict) -> Unified:
    return Unified(
        uid=f"github:{item.get('id')}",
        source="github_repo",
        source_id=str(item.get("id")),
        title=item.get("name"),
        body=item.get("description"),
        author_id=item["owner"]["login"] if item.get("owner") else None,
        fetched_at=datetime.utcnow()
    )
