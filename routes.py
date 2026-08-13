from fastapi import FastAPI
from players import get_players as gt_plys ,get_player as gt_ply, add_players, patch_players, replace_player, rm_players
from blueprint import PlayerCreate,PlayerUpdate,PlayerReplace
from teams import get_teams as teams
from teams import get_team_players as tm_plys
from fastapi.responses import JSONResponse



app=FastAPI()

@app.get("/players")
def player_details(role:str | None=None,country:str | None=None,style:str | None=None ,skip:int = 0,limit:int | None = None):
# def player_details(player:PlayerCreate,skip:int=0,limit:int | None=None,role:str | None=None,country:str | None=None,style:str | None=None):
    return gt_plys(role,country,style,skip,limit)


@app.get("/players/{player_id}")
def player_details(player_id:int):
    return gt_ply(player_id)

@app.get("/teams")
def get_teams():
    return teams()

@app.get("/teams/{player_country}/players")
def get_team(player_country):
    return tm_plys(player_country)

@app.post("/players")
def create_player(player:PlayerCreate):
    add_players(player)
    return JSONResponse(status_code=201, content={"Message":"Invalid Request"})
    
@app.patch("/players/{player_id}")
def update_player(player_id:int,player:PlayerUpdate):
    patch_players(player_id,player)

@app.put("/players/{player_id}")#forgot / -> /players
def put_player(player_id:int,player:PlayerReplace):
    replace_player(player_id,player)

@app.delete("/players/{player_id}")
def del_player(player_id:int):
    rm_players(player_id)


    
# commented or incorrect codes:

# def search(country:str = None,role:str = None ):
#     player={"player_team":player_country, "role":role}
#     return player
