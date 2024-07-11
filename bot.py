import os
from twitchio.ext import commands
from dotenv import load_dotenv
from tinydb import TinyDB, Query
from pkmngen import *

db = TinyDB('db.json')


load_dotenv()

TOKEN = os.getenv("TOKEN")
CHANNELS = os.getenv("CHANNELS").split(',')


DISCORD_INVITE=os.getenv('DISCORD_INVITE')

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=TOKEN, prefix='?', initial_channels=CHANNELS)

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        if message.echo:
            return
        print(message.content)
        await self.handle_commands(message)
    
    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command()
    async def discord(self, ctx: commands.Context):
        await ctx.send(f"Join our Discord at {DISCORD_INVITE}")

    @commands.command()
    async def dance(self, ctx: commands.Context):
        await ctx.send("sumcorSHINYSPROUT sumcorSHINYSPROUT sumcorSHINYSPROUT sumcorSHINYSPROUT")

    @commands.command()
    async def pokegen(self, ctx: commands.Context):
        if not ctx.message.author.is_subscriber:
            await ctx.send("Only subscribers can generate Pokemon")
            return
        if check_pok(ctx.author.name):
            Check = Query()
            pok = trainer_table.get(Check.name == ctx.author.name)
            await ctx.send(f"{ctx.author.name} already generated a {pok['pokemon']}")
        else:
            i = gen_pok()
            trainer_table.insert({{"name": ctx.author.name}, {"pokemon": i}})
            await ctx.send(f"{ctx.author.name}'s random Pokemon is {i}!")

    @commands.command()
    async def schedule(self, ctx: commands.Context):
        await ctx.send("Cob usually streams all days except Mondays and Fridays starting at 11AM EST")

    @commands.command()
    async def suggest(self, ctx: commands.Context, suggestion):
        sug = open("suggestions.txt","a")
        sug.write(f"{suggestion}")
        sug.close()
        await ctx.send(f"Thanks for the suggestion, {ctx.author.name}. It has been logged and will be reviewed!")

    @commands.command()
    async def barry(self, ctx: commands.Context):
        await ctx.send("Barry is a big ol bitch")

    @commands.command(name="lol")
    async def lol(self, ctx: commands.Context):
        table = db.table("pokemon")
        table.insert({"name": "Raichu"})

        
    @commands.command(name="lol2")
    async def lol2(self, ctx: commands.Context):
        table = db.table("pokemon")
        Pokemon = Query()
        test = table.search(Pokemon.name == "Pikachu")
        await ctx.send(f"{test}")



CobBot = Bot()

CobBot.run()

