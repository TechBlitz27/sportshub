from blueprint import PlayerCreate, PlayerUpdate,PlayerReplace,PlayerDelete
import utils
from fastapi import HTTPException
#from db import get_db as db- db.py converted to .json on 10-8-26

def get_players(role:str | None=None,country:str | None=None,style:str | None=None,skip:int | None = None,limit:int | None=None):
  data=utils.load_info()
  req=[] 
  for p in data: 
    if role and p["role"]!=role: 
      continue 
    if country and p["player_country"]!=country: 
      continue
    if (style and p["batting_style"]!=style): 
      continue 
    if (style and p["bowling_style"]!=style):
      continue

    req.append(p)
    #if limit>1->incorrect, correct:
  if skip is not None and limit is not None:
    return req[skip:skip+limit]
  return req
  
  
#print(get_players())

def get_player(pid:int):
  data=utils.load_info()
  for p in data:
    if p["player_id"]==pid:
      return p
  else:
    raise HTTPException(status_code=404)
  
    








def add_players(player:PlayerCreate):
  data=utils.load_info()
  
  for p in data:
    if p["player_id"]==player.player_id:
      raise HTTPException(status_code=400, detail='Player Already Exist')
  
  add=player.model_dump()
  data.append(add)
  utils.save_player_data(data)
  return player
  


def patch_players(player_id:int,player:PlayerUpdate):
  data=utils.load_info()
  # new_country:str = None
  for p in data:
    if p["player_id"]==player_id:
      p["player_country"]=player.new_country
      break
  else:
    raise HTTPException(status_code=404, detail="INVALID REQUEST")    
  utils.save_player_data(data)
