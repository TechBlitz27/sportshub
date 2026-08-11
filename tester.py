import requests
import time

BASE_URL = "http://127.0.0.1:8000"

# Generate a new ID so repeated testing doesn't immediately collide
NEW_ID = int(time.time())

passed = 0
failed = 0


def test(name, condition, response):
    global passed, failed

    if condition:
        print(f"PASS  {name} -> {response.status_code}")
        passed += 1
    else:
        print(f"FAIL  {name} -> {response.status_code}")
        print(response.text)
        failed += 1


# --------------------------------------------------
# GET /players
# --------------------------------------------------

r = requests.get(f"{BASE_URL}/players")

test(
    "GET all players",
    r.status_code == 200 and isinstance(r.json(), list),
    r
)


# --------------------------------------------------
# GET /players?limit=10
# --------------------------------------------------

r = requests.get(
    f"{BASE_URL}/players",
    params={"limit": 10}
)

test(
    "GET players with limit",
    r.status_code == 200 and len(r.json()) <= 10,
    r
)


# --------------------------------------------------
# GET /players?skip=10&limit=10
# --------------------------------------------------

r = requests.get(
    f"{BASE_URL}/players",
    params={
        "skip": 10,
        "limit": 10
    }
)

test(
    "GET players pagination",
    r.status_code == 200 and len(r.json()) <= 10,
    r
)


# --------------------------------------------------
# GET role filter
# --------------------------------------------------

r = requests.get(
    f"{BASE_URL}/players",
    params={"role": "Batter"}
)

role_ok = (
    r.status_code == 200
    and all(player["role"] == "Batter" for player in r.json())
)

test(
    "GET players role filter",
    role_ok,
    r
)


# --------------------------------------------------
# GET country filter
# --------------------------------------------------

r = requests.get(
    f"{BASE_URL}/players",
    params={"country": "India"}
)

country_ok = (
    r.status_code == 200
    and all(
        player["player_country"] == "India"
        for player in r.json()
    )
)

test(
    "GET players country filter",
    country_ok,
    r
)


# --------------------------------------------------
# GET multiple filters
# --------------------------------------------------

r = requests.get(
    f"{BASE_URL}/players",
    params={
        "country": "India",
        "role": "Batter"
    }
)

multiple_filter_ok = (
    r.status_code == 200
    and all(
        player["player_country"] == "India"
        and player["role"] == "Batter"
        for player in r.json()
    )
)

test(
    "GET multiple filters",
    multiple_filter_ok,
    r
)


# --------------------------------------------------
# GET individual existing player
# --------------------------------------------------

r = requests.get(
    f"{BASE_URL}/players/1"
)

test(
    "GET existing player",
    r.status_code == 200,
    r
)


# --------------------------------------------------
# GET nonexistent player
# --------------------------------------------------

r = requests.get(
    f"{BASE_URL}/players/999999"
)

test(
    "GET nonexistent player -> 404",
    r.status_code == 404,
    r
)


# --------------------------------------------------
# POST new player
# --------------------------------------------------

new_player = {
    "player_id": NEW_ID,
    "name": "Test Player",
    "player_country": "India",
    "role": "Batter",
    "batting_style": "Right-hand",
    "bowling_style": None
}

r = requests.post(
    f"{BASE_URL}/players",
    json=new_player
)

test(
    "POST new player",
    r.status_code == 201,
    r
)


# --------------------------------------------------
# GET newly created player
# --------------------------------------------------

r = requests.get(
    f"{BASE_URL}/players/{NEW_ID}"
)

test(
    "GET newly created player",
    r.status_code == 200,
    r
)


# --------------------------------------------------
# POST duplicate player
# --------------------------------------------------

r = requests.post(
    f"{BASE_URL}/players",
    json=new_player
)

test(
    "POST duplicate player -> 400",
    r.status_code == 400,
    r
)


# --------------------------------------------------
# POST invalid type
# --------------------------------------------------

invalid_player = {
    "player_id": "not-an-integer",
    "name": "Invalid Player",
    "player_country": "India",
    "role": "Batter"
}

r = requests.post(
    f"{BASE_URL}/players",
    json=invalid_player
)

test(
    "POST invalid player -> 422",
    r.status_code == 422,
    r
)


# --------------------------------------------------
# POST missing required field
# --------------------------------------------------

missing_field = {
    "player_id": NEW_ID + 1,
    "player_country": "India",
    "role": "Batter"
}

r = requests.post(
    f"{BASE_URL}/players",
    json=missing_field
)

test(
    "POST missing name -> 422",
    r.status_code == 422,
    r
)


# --------------------------------------------------
# SUMMARY
# --------------------------------------------------

print("\n-----------------------------")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print("-----------------------------")