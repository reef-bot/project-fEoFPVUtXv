# ban.py

import discord
from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ban', help='Ban a user from the server')
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if ctx.author.guild_permissions.ban_members:
            if member == ctx.author:
                await ctx.send("You cannot ban yourself.")
            else:
                await member.ban(reason=reason)
                await ctx.send(f'{member} has been banned from the server.')
        else:
            await ctx.send("You do not have permission to ban users.")

def setup(bot):
    bot.add_cog(Ban(bot))