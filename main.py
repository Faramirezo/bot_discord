import discord, os, audioop, logic as l, commandapi as ca
from dotenv import load_dotenv
import random as r
from discord.ext import commands
load_dotenv ()
token = os.getenv("dt")
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command(name = "coin")
async def gamble(ctx):
    await ctx.send(l.coin())

@bot.command(name= "fde")
async def password(ctx, lenght = 25):
    x = l.contra(lenght)
    await ctx.send(f"🔐 su contraseña se ha generado: {x}")

@bot.command(name= "momo")
async def bromas(ctx):
    x = l.momo()
    await ctx.send(file = x)

@bot.command(name= "pato")
async def patos(ctx):
    x = ca.duck_image()
    await ctx.send(x)

bot.run(token)