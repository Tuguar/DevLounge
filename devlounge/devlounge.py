from redbot.core import commands

class Devlounge(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def cmds(self, ctx):
        await ctx.send("**Commands:**\n\n`>pydocs` - Links the Python documentation\n`>dpydocs` - Links the Discord.py documentation\n`>jdocs` - Links the Java documentation\n`>jsdocs` - Links the JavaScript documentation\n`>djsdocs` - Links the Discord.js documentation\n`>cppdocs` - Links the C++ documentation\n`>wc` - Gives a talk about being in the wrong channel")

    @commands.command()
    async def pydocs(self, ctx):
        await ctx.send("It looks like you are looking for the `Python` documentation, here;\nhttps://docs.python.org/3/")
       
    @commands.command()
    async def dpydocs(self, ctx):
        await ctx.send("It looks like you are looking for the `Discord.py` documentation, here;\nhttps://discordpy.readthedocs.io/en/latest/")
       
    @commands.command()
    async def jdocs(self, ctx):
        await ctx.send("It looks like you are looking for the `Java` documentation, here;\nhttps://docs.oracle.com/en/java/")
       
    @commands.command()
    async def jsdocs(self, ctx):
        await ctx.send("It looks like you are looking for the `JavaScript` documentation, here;\nhttps://devdocs.io/javascript/")
        
    @commands.command()
    async def djsdocs(self, ctx):
        await ctx.send("It looks like you are looking for the `Discord.js` documentation, here;\nhttps://discord.js.org/#/docs/main/stable/general/welcome")
        
    @commands.command()
    async def cppdocs(self, ctx):
        await ctx.send("It looks like you are looking for the `C++` documentation, here;\nhttps://devdocs.io/cpp/")
     
    @commands.command()
    async def wc(self, ctx):
        await ctx.send("Your question or statement isn't right for this channel, please move it to the appropiate one.")