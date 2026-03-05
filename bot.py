import discord
import requests

# YOUR DATA
TOKEN = "MTQ3ODkyOTg3MDQ3NzE5NzMzMg.G1bYM9.MScCAWu8Q-emZMKuYFs9Mu_byk4Oxq3OstqRTs"
BRIDGE_URL = "https://brainrotbridge.onrender.com/update"
SOURCE_CHANNEL_ID = 1478761257065644092 # The channel where brainrot is sent

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

    # Check if the message is in the correct channel and has the right format
    if message.channel.id == SOURCE_CHANNEL_ID and "name=" in message.content:
        try:
            # Pushes the text to your Render bridge
            requests.post(BRIDGE_URL, data=message.content)
            print("Sent data to Roblox Bridge!")
        except Exception as e:
            print(f"Error: {e}")

client.run(TOKEN)
