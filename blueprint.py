from pydantic import BaseModel
from typing import Optional

class PlayerCreate(BaseModel):
  player_id: int
  name: str
  player_country: str
  role: str
  batting_style: Optional[str]=None
  bowling_style: Optional[str]=None

class PlayerUpdate(BaseModel):
  new_country: str

class PlayerReplace(BaseModel):
  name: str
  player_country: str
  role: str
  batting_style: Optional[str]=None
  bowling_style: Optional[str]=None

class PlayerDelete(BaseModel):
  pass