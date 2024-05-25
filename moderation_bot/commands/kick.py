# File: kick.py

import discord
from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick')
    async def kick_member(self, ctx, member: discord.Member, *, reason=None):
        if ctx.author.guild_permissions.kick_members:
            if ctx.author.top_role > member.top_role:
                await member.kick(reason=reason)
                await ctx.send(f'{member.mention} has been kicked from the server.')
            else:
                await ctx.send('You do not have permission to kick this member.')
        else:
            await ctx.send('You do not have permission to use this command.')

def setup(bot):
    bot.add_cog(Kick(bot))