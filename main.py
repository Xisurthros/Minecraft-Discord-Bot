import discord
from discord.ext import commands
import random
import os
from datetime import datetime


print('Bot is running')

print(discord.__version__)

# This creates and determines the command prefix
client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

client.remove_command('help')


# This changes this game status for the bot
@client.event
async def on_ready():
    activity = discord.Game(name="minecraft | .mchelp")
    await client.change_presence(status=discord.Status.online, activity=activity)


# This will create a custom help command
@client.command(pass_context=True)
async def mchelp(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        title='Minecraft Controls',
        colour=discord.Colour.dark_gold(),
        timestamp=datetime.utcnow(),
    )
    embed.set_thumbnail(url='https://images.discordapp.net/avatars/616308233950199828/355ff6e9b639e7cebfc4a85e9c4e3ce5.png?size=512')
    embed.set_footer(text='This bot was created by Dzakar#1693')
    embed.add_field(name='.mine, [.m]', value='.m (time in seconds) to mine', inline=False)
    embed.add_field(name='.place, [.p]', value='.p place an item', inline=False)
    embed.add_field(name='.walk_forward, [.wf]', value='.wf (time in seconds) to walk forward', inline=False)
    embed.add_field(name='.run_forward, [.rf]', value='.rf (time in seconds) to run forward', inline=False)
    embed.add_field(name='.run_jump_forward, [.rjf]', value='.rjf (time in seconds) to run jump forward', inline=False)
    embed.add_field(name='.walk_right, [.wr]', value='.wr (time in seconds) to sideways right', inline=False)
    embed.add_field(name='.walk_left, [.wl]', value='.wl (time in seconds) to sideways left', inline=False)
    embed.add_field(name='.walk_backward, [.wb]', value='.wb (time in seconds) to walk backwards', inline=False)
    embed.add_field(name='.look_left, [.ll]', value='.ll (22, 45, 90, 180)degrees to turn left', inline=False)
    embed.add_field(name='.look_right, [.lr]', value='.lr (22, 45, 90, 180)degrees to turn right', inline=False)
    embed.add_field(name='.look_up, [.lu]', value='.lu (22, 45, 90, 180)degrees to look up', inline=False)
    embed.add_field(name='.look_down, [.ld]', value='.ld (22, 45, 90, 180)degrees to look down', inline=False)
    embed.add_field(name='.chat, [.t][.c]', value='.t (message) to send a message in game', inline=False)

    await ctx.send(embed=embed)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# This is the client TOKEN
client.run('Nzk4NjMyODI0NzA1MjUzNDA2.X_32xw.k6ELDhACL2PMDWF_k6DQBzUKDJc')
