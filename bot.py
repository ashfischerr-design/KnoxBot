import discord
import requests
from flask import Flask
from threading import Thread
import os

# 1. THE KEEP ALIVE SERVER (For Koyeb Health Checks)
app = Flask('')

@app.route('/')
def home():
    return "Knox Bot is Alive and Running!"

def run():
    # Koyeb uses port 8080 by default for free tier
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 2. THE DISCORD BOT LOGIC
TOKEN = "MTQ3ODkyOTg3MDQ3NzE5NzMzMg.G1bYM9.MScCAWu8Q-emZMKuYFs9Mu_byk4Oxq3OstqRTs"
BRIDGE_URL = "https://brainrotbridge.onrender.com/update"
SOURCE_CHANNEL_ID = 1478761257065644092

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Check for the Brainrot message format
    if message.channel.id == SOURCE_CHANNEL_ID and "name=" in message.content:
        try:
            # Send the data to your Render Bridge
            requests.post(BRIDGE_URL, data=message.content)
            print("Successfully updated the Bridge!")
        except Exception as e:
            print(f"Error updating Bridge: {e}")

# 3. START EVERYTHING
if __name__ == "__main__":
    keep_alive() # Starts the Flask server in the background
    client.run(TOKEN) # Starts the Discord bot
