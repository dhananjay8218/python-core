from typing import List, Optional
from pydantic import BaseModel


# Recursive model for nested comments / replies
class Comment(BaseModel):
    id: int
    content: str
    # Forward reference allows a model to reference itself
    replies: Optional[List["Comment"]] = None


# Resolve forward references
Comment.model_rebuild()


# Example nested comment structure
comment = Comment(
    id=1,
    content="First comment",
    replies=[
        Comment(id=2, content="Reply 1"),
        Comment(
            id=3,
            content="Reply 2",
            replies=[
                Comment(id=4, content="Nested reply")
            ]
        )
    ]
)

print(comment)
