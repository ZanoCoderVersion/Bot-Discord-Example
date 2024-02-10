import discord
from discord.ext import commands
from discord import Intents, Status, Game

bot = commands.Bot(command_prefix={"!","?","."}, intents=Intents.all())

@bot.event
async def on_ready()
    print(f"Logged in as {bot.user}")
    await bot.change_presence(status=Status.online, activity=Game(name="HERE'S IT'S EXAMPLE DISCORD BOT PYTHON"))
    try:
      sync = await bot.tree.sync()
      print(f"Synced {len(sync)}command")
    except Exception as e:
      print(e)

@bot.command()
async def hello(ctx):
  await ctx.send(f"Hi!, I'm {bot.user}")


bot.run("") # PUT YOUR TOKEN ID
