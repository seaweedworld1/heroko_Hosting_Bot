import discord
from discord.ext import commands
client = discord.Client()
import json
import datetime
import googletrans
import os
from pprint import pprint
intents = discord.Intents.all()

bot = commands.Bot(command_prefix= '[')

# 輸入自己Bot的TOKEN碼
TOKEN = os.environ['TOKEN']
channel_1 = os.environ['channel_1']
SRCLanguage=os.environ['SRC']
DSTLanguage=os.environ['DST']



# 起動時呼叫
@client.event
async def on_ready():
    print(">> Bot is online 🟢 <<")
    
@bot.command()
async def ping(ctx):
    await ctx.send(f'現在延遲 ➡ {round(bot.latency*1000)}(ms)')
    
@bot.command()
async def open(ctx):
    await ctx.send('伺服器狀態已更改：🟢')
    activity = discord.Game(name="奈何之都狀態：🟢")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    channel = bot.get_channel(int(channel_1))
    await channel.send('伺服器狀態：🟢已開啟　')
    await channel.send('－－－－登入方式－－－－')
    await channel.send('使用F8 connect 1.34.120.212')
    await channel.send('點選網址： https://cfx.re/join/m3lzqq')
    await channel.send('@everyone ')

@bot.command()
async def ten(ctx):
    await ctx.send('伺服器狀態已更改：十分鐘後重啟🔄')
    activity = discord.Game(name="奈何之都狀態：十分鐘後重啟🔄", type=2)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    channel = bot.get_channel(int(channel_1))
    await channel.send('伺服器狀態：🔄十分鐘後重啟　')
    await channel.send('@everyone ')

@bot.command()
async def five(ctx):
    await ctx.send('伺服器狀態已更改：五分鐘後重啟🔄')
    activity = discord.Game(name="奈何之都狀態：五分鐘後重啟🔄", type=2)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    channel = bot.get_channel(int(channel_1))
    await channel.send('伺服器狀態：🔄五分鐘後重啟　')
    await channel.send('@everyone ')

@bot.command()
async def close(ctx):
    await ctx.send('伺服器狀態已更改：🔴')
    activity = discord.Game(name="奈何之都狀態：🔴", type=2)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    channel = bot.get_channel(int(channel_1))
    await channel.send('伺服器狀態：🔴已關閉　')

# Bot起動
client.run(TOKEN)
