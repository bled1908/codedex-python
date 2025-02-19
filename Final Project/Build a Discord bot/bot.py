# import discord
# import requests
# import json
# import os

# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# def get_meme():
#   response = requests.get('https://meme-api.com/gimme')
#   json_data = json.loads(response.text)
#   return json_data['url']

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print('Logged on as {0}!'.format(self.user))
    
#     async def on_message(self, message):
#         if message.author == self.user:
#             return
#         if message.content.startswith('$meme'):
#             await message.channel.send(get_meme())
        
#         if message.content.startswith('$hello'):
#             await message.channel.send('Hello World!')

# intents = discord.Intents.default()
# intents.message_content = True

# client = MyClient(intents=intents)
# client.run('API token') # Replace with your own token.


import discord
import aiohttp
import json
import os
from dotenv import load_dotenv
import random

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Set to store previously sent meme URLs
sent_memes = set()

async def get_meme():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://meme-api.com/gimme/1') as response:
            if response.status == 200:
                json_data = await response.json()
                meme_url = json_data['memes'][0]['url']
                
                # If the meme has already been sent, get a new one
                while meme_url in sent_memes:
                    async with session.get('https://meme-api.com/gimme/1') as response:
                        json_data = await response.json()
                        meme_url = json_data['memes'][0]['url']
                
                # Add the meme to the sent set
                sent_memes.add(meme_url)
                
                # Optional: Limit the cache size to avoid memory bloat
                if len(sent_memes) > 100:  # Store only the last 100 memes
                    sent_memes.pop()
                
                return meme_url
            return "Couldn't fetch a meme at the moment."

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('$meme'):
            meme_url = await get_meme()  # Await async function
            await message.channel.send(meme_url)
        
        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)  # Uses secure environment variable
