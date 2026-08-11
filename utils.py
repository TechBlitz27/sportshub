import json

def load_info():
    with open('data.json','r') as f:
        data=json.load(f)
    return data

def save_player_data(player):
    with open('data.json','w') as f:
        json.dump(player, f)
        
    