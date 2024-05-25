# helpers.py

import discord
from discord.ext import commands

class Helpers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def get_moderation_log_channel(self, guild):
        for channel in guild.text_channels:
            if channel.name == 'moderation-log':
                return channel
        return None

    async def log_action(self, action, user, moderator, reason):
        embed = discord.Embed(title=f'{action} Action', color=discord.Color.red())
        embed.add_field(name='User', value=user, inline=False)
        embed.add_field(name='Moderator', value=moderator, inline=False)
        embed.add_field(name='Reason', value=reason, inline=False)
        embed.timestamp = datetime.datetime.utcnow()

        log_channel = await self.get_moderation_log_channel(user.guild)
        if log_channel:
            await log_channel.send(embed=embed)
        else:
            print('Moderation log channel not found.')

    async def send_dm(self, user, message):
        try:
            await user.send(message)
        except discord.Forbidden:
            print(f'Failed to send DM to {user.name}. User has DMs disabled.')

    async def get_member(self, ctx, member_id):
        try:
            member = await commands.MemberConverter().convert(ctx, member_id)
            return member
        except commands.MemberNotFound:
            return None

    async def get_user(self, ctx, user_id):
        try:
            user = await commands.UserConverter().convert(ctx, user_id)
            return user
        except commands.UserNotFound:
            return None

    async def get_guild(self, ctx, guild_id):
        try:
            guild = self.bot.get_guild(guild_id)
            return guild
        except commands.GuildNotFound:
            return None

    async def get_channel(self, ctx, channel_id):
        try:
            channel = self.bot.get_channel(channel_id)
            return channel
        except commands.ChannelNotFound:
            return None
