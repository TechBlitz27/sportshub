
def get_teams():
  teams=["India", "Australia", "Bangladesh", "New Zealand", "South Africa","England","Ireland","SriLanka" ,"WestINdies" ,"Afghanistan"]
  return teams

def get_team_players(player_country):
  #team_players=[] #country,role etc sort k liye ek empty list pehle banani chahiye
  req=[]
  for players in db():
    if players["player_country"]==player_country:
      req.append(players)
      #return team_players loop k bahar return karna chahiye
  return req
