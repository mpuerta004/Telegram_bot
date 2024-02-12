from typing import Any, Dict, Optional, Union, List

from sqlalchemy.orm import Session
from fastapi import HTTPException

from crud.base import CRUDBase
from models.last_user_position import Last_user_position
from schemas.last_user_position import Last_user_positionCreate, Last_user_positionUpdate, Last_user_positionSearchResults
from fastapi.encoders import jsonable_encoder
from sqlalchemy import and_, extract
from sqlalchemy import func

class CRUDLast_user_position(CRUDBase[Last_user_position, Last_user_positionCreate, Last_user_positionUpdate]):
    
     def get_by_id(self, db: Session, *, member_id:int) -> Optional[Last_user_position]:
          try:
              return db.query(Last_user_position).filter(and_(Last_user_position.member_id == member_id)).first()
          except Exception as e:
                        raise HTTPException(status_code=500, detail=f"Error with mysql {e}" )
   
        
     def remove(self, db: Session, *, Last_user_position:Last_user_position) -> Last_user_position:
          try:
               obj = Last_user_position
               db.delete(obj)
               db.commit()
               return obj
          except Exception as e:
                        raise HTTPException(status_code=500, detail=f"Error with mysql {e}" )
   
        
   
     def create_member(self, db: Session, *, obj_in: Last_user_positionCreate,id:int) -> Last_user_position:
              try:
                     obj_in_data = jsonable_encoder(obj_in) 
                     db_obj = self.model(**obj_in_data,id=id)  # type: ignore
                     db.add(db_obj)
                     db.commit()
                     db.refresh(db_obj)
                     return db_obj
              except Exception as e:
                            raise HTTPException(status_code=500, detail=f"Error with mysql {e}" )
       


last_user_position = CRUDLast_user_position(Last_user_position)
