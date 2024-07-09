from twitchio.ext import commands

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token="", prefix='?', initial_channels=[''])

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
    async def 


CobBot = Bot()

CobBot.run()

