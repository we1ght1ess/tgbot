import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print("Бот готов к работе")

@client.command()
async def go(ctx):
    await ctx.send("Привет, я бот")

client.run("ТОКЕН")

bot.run('5e33883ada9cbb6fac41899600a985417faea24cc041bffeb95ae508bbdc4ef3')