from typing import Optional, List, Sequence
from pydantic import BaseModel
from datetime import datetime, timezone
from enum import Enum
import numpy as np

    
class gender_type(str, Enum):
    MALE="MALE"
    NOBINARY="NOBINARY"
    FEMALE="FEMALE"
    NOANSWER ='NOANSWER' 
    

class MemberBase(BaseModel):
    name: str 
    surname: str=None
    age: int
    gender:gender_type
    city: str=None
    mail:str
    birthday:datetime
    # device_id:int=None


# Properties to receive via API on creation
class MemberCreate(MemberBase):
    id:int
    pass
    

# Properties to receive via API on update
class MemberUpdate(MemberBase):
    pass


class MemberInDBBase(MemberBase):
    id: int = None
    
    class Config:
        orm_mode = True


# Additional properties to return via API
class Member(MemberInDBBase):
    pass

# Properties properties stored in DB
class MemberInDB(MemberInDBBase):
    pass


class MemberSearchResults(BaseModel):
    results: Sequence[Member]

