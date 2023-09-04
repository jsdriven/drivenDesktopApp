from pydantic import BaseModel, Field
from datetime import datetime
from typing import List
from bson import ObjectId

class Post(BaseModel):
        id: str = Field(..., alias="_id")
        title: str = Field(...)
        tags: List[str] = Field(...)
        content: str  = Field(...)
        description: str  = Field(...)
        postDate: datetime  = Field(...)
        comments: List[str]  = Field(...)
        likes: List[str]  = Field(...)
        
        def TagsToString(self):
            return ",".join(self.tags)
        
        class Config:
            populate_by_name=True
            arbitrary_types_allowed = True
            json_encoders = {ObjectId: str}
            
#Need to implement a UpdatePost Model as well for editing