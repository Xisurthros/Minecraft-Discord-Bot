import discord
from discord.ext import commands
from discord import Embed
import pydirectinput
import time


class Controls(commands.Cog):
    author = 198667876138221568

    def __init__(self, bot):
        self.bot = bot

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Controls are running...')

    @commands.command(aliases=['m'], description='.m (seconds) to mine')
    async def mine(self, ctx, *, x):
        try:

            if float(x) <= 0 or float(x) >= 30:
                await ctx.send(f'Try again and enter a number greater than 0 and less than 20')

            else:
                pydirectinput.mouseDown()
                time.sleep(int(x))
                pydirectinput.mouseUp()


        except:
            await ctx.send(f'Unexpected Error. Try again later')
            await ctx.author.send(f'walk_forward error in: {ctx.guild.id}/{ctx.guild.id}')

    @commands.command(aliases=['p'], description='.p place an item')
    async def place(self, ctx):
        try:
            pydirectinput.mouseDown(button='right')

        except:
            await ctx.send(f'Unexpected Error. Try again later')
            await ctx.author.send(f'walk_forward error in: {ctx.guild.id}/{ctx.guild.id}')

    # Movement Commands
    @commands.command(aliases=['wf'], description='.wf (time in seconds) to walk forward')
    async def walk_forward(self, ctx, *, x):
        try:

            if float(x) <= 0 or float(x) >= 20:
                await ctx.send(f'Try again and enter a number greater than 0 and less than 20')

            else:
                pydirectinput.keyDown('w')
                time.sleep(int(x))
                pydirectinput.keyUp('w')

        except:
            await ctx.send(f'Unexpected Error. Try again later')
            await ctx.author.send(f'walk_forward error in: {ctx.guild.id}/{ctx.guild.id}')

    @commands.command(aliases=['rf'], description='.rf (time in seconds) to run forward')
    async def run_forward(self, ctx, *, x):
        try:

            if float(x) <= 0 or float(x) >= 20:
                await ctx.send(f'Try again and enter a number greater than 0 and less than 20')

            else:
                pydirectinput.keyDown('ctrl')
                pydirectinput.keyDown('w')
                time.sleep(int(x))
                pydirectinput.keyUp('ctrl')
                pydirectinput.keyUp('w')

        except:
            await ctx.send(f'Unexpected Error. Try again later')
            await ctx.author.send(f'run_forward error in: {ctx.guild.id}/{ctx.guild.id}')

    @commands.command(aliases=['rjf'], description='.rjf (time in seconds) to run jump forward')
    async def run_jump_forward(self, ctx, *, x):
        try:

            if float(x) <= 0 or float(x) >= 20:
                await ctx.send(f'Try again and enter a number greater than 0 and less than 20')

            else:
                x1 = int(x)
                x2 = 0
                pydirectinput.keyDown('ctrl')
                pydirectinput.keyDown('w')

                while x2 != x1:
                    pydirectinput.press('space')
                    time.sleep(0.3)
                    x2 += 1
                    pydirectinput.keyUp('ctrl')
                    pydirectinput.keyUp('w')

        except:
            await ctx.send(f'Unexpected Error. Try again later')
            await ctx.author.send(f'run_jump_forward error in: {ctx.guild.id}/{ctx.guild.id}')

    @commands.command(aliases=['wr'], description='.wr (time in seconds) to walk forward')
    async def walk_right(self, ctx, *, x):
        try:

            if float(x) <= 0 or float(x) >= 20:
                await ctx.send(f'Try again and enter a number greater than 0 and less than 20')

            else:
                pydirectinput.keyDown('d')
                time.sleep(int(x))
                pydirectinput.keyUp('d')

        except:
            await ctx.send(f'Unexpected Error. Try again later')
            await ctx.author.send(f'walk_right error in: {ctx.guild.id}/{ctx.guild.id}')

    @commands.command(aliases=['wl'], description='.wr (time in seconds) to walk forward')
    async def walk_left(self, ctx, *, x):
        try:

            if float(x) <= 0 or float(x) >= 20:
                await ctx.send(f'Try again and enter a number greater than 0 and less than 20')

            else:
                pydirectinput.keyDown('a')
                time.sleep(int(x))
                pydirectinput.keyUp('a')

        except:
            await ctx.send(f'Unexpected Error. Try again later')
            await ctx.author.send(f'walk_left error in: {ctx.guild.id}/{ctx.guild.id}')

    @commands.command(aliases=['wb'], description='.wb (time in seconds) to walk forward')
    async def walk_backward(self, ctx, *, x):
        try:

            if float(x) <= 0 or float(x) >= 20:
                await ctx.send(f'Try again and enter a number greater than 0 and less than 20')

            else:
                pydirectinput.keyDown('s')
                time.sleep(int(x))
                pydirectinput.keyUp('s')

        except:
            await ctx.send(f'Unexpected Error. Try again later')
            await ctx.author.send(f'walk_backward error in: {ctx.guild.id}/{ctx.guild.id}')

    # Look commands
    @commands.command(aliases=['ll'], description='.lf (22, 45, 90, 180)degrees to turn left')
    async def look_left(self, ctx, x):
        try:

            if '22' in x:
                pydirectinput.move(-149, 0, 5)

            elif '45' in x:
                pydirectinput.move(-298, 0)

            elif '90' in x:
                pydirectinput.move(-594, 0)

            elif '180' in x:
                pydirectinput.move(-1192, 0)

            else:
                await ctx.send(f'Try again with a (22, 45, 90, 180)')

        except:
            await ctx.send(f'Unexpected Error. Try again later')
            await ctx.author.send(f'look_left error in: {ctx.guild.id}/{ctx.guild.id}')

    @commands.command(aliases=['lr'], description='.lr (22, 45, 90, 180)degrees to turn right')
    async def look_right(self, ctx, x):
        try:

            if '22' in x:
                pydirectinput.move(149, 0)

            if '45' in x:
                pydirectinput.move(298, 0)

            if '90' in x:
                pydirectinput.move(596, 0)

            if '180' in x:
                pydirectinput.move(1192, 0)

            else:
                await ctx.send(f'Try again with a (22, 45, 90, 180)')

        except:
            await ctx.send(f'Unexpected Error. Try again later')
            await ctx.author.send(f'look_right error in: {ctx.guild.id}/{ctx.guild.id}')

    @commands.command(aliases=['lu'], description='.lu (22, 45, 90)degrees to look up')
    async def look_up(self, ctx, x):
        try:

            if '22' in x:
                pydirectinput.move(0, -149)

            if '45' in x:
                pydirectinput.move(0, -298)

            if '90' in x:
                pydirectinput.move(0, -1000)

            if '180' in x:
                pydirectinput.move(0, -1192)

            else:
                await ctx.send(f'Try again with a (22, 45, 90, 180)')

        except:
            await ctx.send(f'Unexpected Error. Try again later')
            await ctx.author.send(f'look_up error in: {ctx.guild.id}/{ctx.guild.id}')

    @commands.command(aliases=['ld'], description='.lu (22, 45, 90)degrees to look down')
    async def look_down(self, ctx, x):
        try:

            if '22' in x:
                pydirectinput.move(0, 149)

            if '45' in x:
                pydirectinput.move(0, 298)

            if '90' in x:
                pydirectinput.move(0, 620)

            if '180' in x:
                pydirectinput.move(0, 1192)

            else:
                await ctx.send(f'Try again with a (22, 45, 90, 180)')

        except:
            await ctx.send(f'Unexpected Error. Try again later')
            await ctx.author.send(f'look_down error in: {ctx.guild.id}/{ctx.guild.id}')

    # Type in gamechat
    @commands.command(aliases=['t', 'c'], description='.t (message)')
    async def chat(self, ctx, *, message):
        try:
            pydirectinput.press('t')
            pydirectinput.write(message)
            pydirectinput.press('enter')

        except:
            await ctx.send(f'Unexpected Error. Try again later')
            await ctx.author.send(f'chat error in: {ctx.guild.id}/{ctx.guild.id}')


def setup(client):
    client.add_cog(Controls(client))
