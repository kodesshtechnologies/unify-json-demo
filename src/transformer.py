# src/transformer.py
from datetime import datetime
from src.model import Unified

def transform_post(item: dict) -> Unified:
    return Unified(
        uid=f"posts:{item.get('id')}",
        source="posts",
        source_id=str(item.get("id")),
        title=item.get("title"),
        body=item.get("body"),
        author_id=str(item.get("userId")) if item.get("userId") else None,
        fetched_at=datetime.utcnow()
    )

def transform_todo(item: dict) -> Unified:
    return Unified(
        uid=f"todos:{item.get('id')}",
        source="todos",
        source_id=str(item.get("id")),
        title=item.get("title"),
        completed=item.get("completed"),
        author_id=str(item.get("userId")) if item.get("userId") else None,
        fetched_at=datetime.utcnow()
    )
