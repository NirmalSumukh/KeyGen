from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import asyncio
import os
import random
from KeyGen import KeyGen
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

app = FastAPI()

origins = [
    "https://hamsterkeys-82696.web.app/",
    "https://hamsterkeys-82696.firebaseapp.com/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Adjust this to allow specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
async def root():
    return RedirectResponse(url="/static/index.html")

# Initialize games dictionary (as you've done before)
games = {
    1: {
        'name': 'Chain Cube 2048',
        'appToken': 'd1690a07-3780-4068-810f-9b5bbf2931b2',
        'promoId': 'b4170868-cef0-424f-8eb9-be0622e8e8e3',
        'timing': 25000 / 1000,
        'attempts': 20,
    },
    2: {
        'name': 'Train Miner',
        'appToken': '82647f43-3f87-402d-88dd-09a90025313f',
        'promoId': 'c4480ac7-e178-4973-8061-9ed5b2e17954',
        'timing': 20000 / 1000,
        'attempts': 15,
    },
    3: {
        'name': 'Merge Away',
        'appToken': '8d1cc2ad-e097-4b86-90ef-7a27e19fb833',
        'promoId': 'dc128d28-c45b-411c-98ff-ac7726fbaea4',
        'timing': 20000 / 1000,
        'attempts': 25,
    },
    4: {
        'name': 'Twerk Race 3D',
        'appToken': '61308365-9d16-4040-8bb0-2f4a4c69074c',
        'promoId': '61308365-9d16-4040-8bb0-2f4a4c69074c',
        'timing': 20000 / 1000,
        'attempts': 20,
    },
    5: {
        'name': 'Polysphere',
        'appToken': '2aaf5aee-2cbc-47ec-8a3f-0962cc14bc71',
        'promoId': '2aaf5aee-2cbc-47ec-8a3f-0962cc14bc71',
        'timing': 20000 / 1000,
        'attempts': 20,
    },
    6: {
        'name': 'Mow and Trim',
        'appToken': 'ef319a80-949a-492e-8ee0-424fb5fc20a6',
        'promoId': 'ef319a80-949a-492e-8ee0-424fb5fc20a6',
        'timing': 20000 / 1000,
        'attempts': 20,
    },
    7: {
        'name': 'Tile Trio',
        'appToken': 'e68b39d2-4880-4a31-b3aa-0393e7df10c7',
        'promoId': 'e68b39d2-4880-4a31-b3aa-0393e7df10c7',
        'timing': 20000 / 1000,
        'attempts': 20,
    },
    8: {
        'name': 'Zoopolis',
        'appToken': 'b2436c89-e0aa-4aed-8046-9b0515e1c46b',
        'promoId': 'b2436c89-e0aa-4aed-8046-9b0515e1c46b',
        'timing': 20000 / 1000,
        'attempts': 20,
    },
    9: {
        'name': 'Fluff Crusade',
        'appToken': '112887b0-a8af-4eb2-ac63-d82df78283d9',
        'promoId': '112887b0-a8af-4eb2-ac63-d82df78283d9',
        'timing': 30000 / 1000,
        'attempts': 20,
    },
    10: {
        'name': 'Stone Age',
        'appToken': '04ebd6de-69b7-43d1-9c4b-04a6ca3305af',
        'promoId': '04ebd6de-69b7-43d1-9c4b-04a6ca3305af',
        'timing': 20000 / 1000,
        'attempts': 20,
    },
   11: {
        'name': 'Bouncemasters',
        'appToken': 'bc72d3b9-8e91-4884-9c33-f72482f0db37',
        'promoId': 'bc72d3b9-8e91-4884-9c33-f72482f0db37',
        'timing': 20000 / 1000,
        'attempts': 20,
    },
    12: {
        'name': 'Hide Ball',
        'appToken': '4bf4966c-4d22-439b-8ff2-dc5ebca1a600',
        'promoId': '4bf4966c-4d22-439b-8ff2-dc5ebca1a600',
        'timing': 40000 / 1000,
        'attempts': 20,
    },
    13: {
        'name': 'Pin Out Master',
        'appToken': 'd2378baf-d617-417a-9d99-d685824335f0',
        'promoId': 'd2378baf-d617-417a-9d99-d685824335f0',
        'timing': 30000 / 1000,
        'attempts': 20,
    },
    14: {
        'name': 'Count Masters',
        'appToken': '4bdc17da-2601-449b-948e-f8c7bd376553',
        'promoId': '4bdc17da-2601-449b-948e-f8c7bd376553',
        'timing': 30000 / 1000,
        'attempts': 20,
    },
    15: {
        'name': 'Infected Frontier',
        'appToken': 'eb518c4b-e448-4065-9d33-06f3039f0fcb',
        'promoId': 'eb518c4b-e448-4065-9d33-06f3039f0fcb',
        'timing': 30000 / 1000,
        'attempts': 20,
    },
    16: {
        'name': 'Among Waterr',
        'appToken': 'daab8f83-8ea2-4ad0-8dd5-d33363129640',
        'promoId': 'daab8f83-8ea2-4ad0-8dd5-d33363129640',
        'timing': 30000 / 1000,
        'attempts': 20,
    },
    17: {
        'name': 'Factory World',
        'appToken': 'd02fc404-8985-4305-87d8-32bd4e66bb16',
        'promoId': 'd02fc404-8985-4305-87d8-32bd4e66bb16',
        'timing': 30000 / 1000,
        'attempts': 20,
    },
}

# Load proxies function
async def load_proxies(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            proxies = [line.strip() for line in file if line.strip()]
            random.shuffle(proxies)
            return proxies
    return []



# Define the request model for key generation
class KeyRequest(BaseModel):
    game_id: int
    key_count: int

@app.get("/games")
async def get_games():
    # Return the list of games
    return {"games": [
            {
                "id": key,
                "name": value['name'],
                "appToken": value['appToken'],
                "promoId": value['promoId'],
                "timing": value['timing'],
                "attempts": value['attempts']
            } 
            for key, value in games.items()
            ]
        }

@app.post("/generate-keys")
async def generate_keys(request: KeyRequest):
    # Validate game ID
    if request.game_id not in games:
        raise HTTPException(status_code=404, detail="Game not found")
    
    # Get game details
    game = games[request.game_id]
    
    # Load proxies
    proxies = await load_proxies("proxies.txt")
    
    # Initialize KeyGen
    keygen = KeyGen(
        app_token=game['appToken'],
        promo_id=game['promoId'],
        proxies=proxies,
        timing=game['timing'],
        attempts=game['attempts']
    )
    print("KeyGen Initialization:")
    print(f"App Token: {game['appToken']}")
    print(f"Promo ID: {game['promoId']}")
    print(f"Proxies: {proxies}")
    print(f"Timing: {game['timing']}")
    print(f"Attempts: {game['attempts']}")

    # Generate keys asynchronously
    keys = []
    for _ in range(request.key_count):
        key = await keygen.generate_keys()
        if key:
            keys.append(key)
        else:
            print("Failed to generate key")
    
    # Return the generated keys
    return {"keys": keys}

# Run the app using Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
