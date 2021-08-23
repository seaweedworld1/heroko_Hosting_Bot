import discord
from discord.ext import commands
import json
import datetime
import googletrans
import os
from pprint import pprint

client = discord.Client()
bot = commands.Bot(command_prefix= '[')

# 輸入自己Bot的TOKEN碼
TOKEN = os.environ['TOKEN']
channel_1 = os.environ['channel_1']
SRCLanguage=os.environ['SRC']
DSTLanguage=os.environ['DST']



# 起動時呼叫
@bot.event
async def on_ready():
    print(">> Bot is online 🟢 <<")
    
@bot.command()
async def ping(ctx):
    await ctx.send(f'現在延遲 ➡ {round(bot.latency*1000)}(ms)')

@bot.command()
async def em(ctx):
    embed=discord.Embed(title="Discord群組", url="https://discord.gg/CyK6HanMvM", description="⬆找製作者請點上方連結", color=0x09a4f1, timestamp= datetime.datetime.utcnow())
    embed.set_author(name="海苔Kevin#4760", icon_url="https://lh3.googleusercontent.com/krH41yRrH5lOJ4a2mnD4jVUe9HjmEQw5E3RL0tkuv5lyqPnTOOPJ0RMyC5j7ubi4rmU-mocMxvsjxZ1NHRi3YGbpLv-av-IsQjecPr7a5G_NFLjakP6RQMVDwMBB-EgJnLPAus4c9i05Ue0IZMXlpmLRe68aA9BsCiav7i2H8Zre3Y7-8H44uZbJraqASH79wB-6SzGFUb89r-xeBRTIfyIysnTCtwXryOsHG7Q9_kG4zfsFm6N26FCLrIe9hfu6ykro5y-ErhaCXINt3CugVnLiaN2j7X5Ni4jD6j0QS5qA3x6lJ1ziJqVL8kEe8eDrSFoYgzRJ3gl0oVLEuDJiuqegbkZhXSB-Abg_1LeR6YyisFTbBYDFQpobkPhnLs8YAWYdf1ZPmoGg9ibA9-ctPSPdyL394vs766IzCVCX_G22t4UeOdc7_RwSKjo7KJZ3NZHxzMtdGssnpnMY-VJfAmMq3TsazfBed6fYM9W2Pre2bKrF3LssWzNUDkfacxICF504a-me3p2hICfOI9eqraI_H4SURTewQmc1Y0JdsX-ANkVoeOPchdKt0UjC3j820sXEao4CNfUufqEV4wTFkb1s0KVM_BuNrawi3HqemRds6ah5GeDb4-qCPWx7ma76dhbDribO0LjB9neDDJiNIvfaDVVYWZxxIWrcEKrGXLKBYWAaTELomoPTOCUV_fMX16wiPgGby7DDa3kZDwXcxSA=s124-no?authuser=0")
    embed.add_field(name="以下是BOT指令", value="===================", inline=False)
    embed.add_field(name="[em", value="差看指令or其他 ", inline=True)
    embed.add_field(name="[ping", value="差看機器人延遲", inline=True)
    embed.add_field(name="伺服器啟動選項", value="===================", inline=False)
    embed.add_field(name="[open", value="伺服器開啟", inline=True)
    embed.add_field(name="[close", value="伺服器關閉", inline=True)
    embed.add_field(name="[five", value="五分鐘後重啟", inline=True)
    embed.add_field(name="[ten", value="十分鐘後重啟", inline=True)
    embed.set_footer(text="Requisitado per 海苔Kevin#4760")
    await ctx.send(embed=embed)


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
