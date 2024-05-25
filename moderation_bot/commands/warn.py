# File: moderation_bot/commands/warn.py

import discord
from discord.ext import commands

class Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='warn', help='Warn a user for their behavior')
    async def warn_user(self, ctx, user: discord.Member, *, reason=None):
        if ctx.message.author.guild_permissions.administrator:
            if reason:
                # Logic to warn the user and log the warning
                await ctx.send(f'{user.mention} has been warned for: {reason}')
            else:
                await ctx.send('Please provide a reason for warning the user.')
        else:
            await ctx.send('You do not have permission to warn users.')

def setup(bot):
    bot.add_cog(Warn(bot))