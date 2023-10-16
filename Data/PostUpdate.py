from pydantic import BaseModel
from typing import List
from typing import Optional

class PostUpdate(BaseModel):
        title: Optional[str] = None
        content: Optional[str] = None
        description: Optional[str] = None 
        tags: Optional[List[str]] = None
        recommendLink: Optional[str] = None
        
        