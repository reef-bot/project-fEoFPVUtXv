# main.py

import discord
from discord.ext import commands
import json

# Import other modules
from config import settings
from utils import logging
from commands import kick, ban, warn, mute
from filters import content_filter, machine_learning
from database import moderation_log

# Initialize bot
bot = commands.Bot(command_prefix='!')

# Load moderation rules from file
with open('config/moderation_rules.json', 'r') as file:
    moderation_rules = json.load(file)

# Bot events
@bot.event
async def on_ready():
    logging.info('Bot is ready.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    # Check message content for inappropriate content
    if content_filter.check_content(message.content):
        await message.delete()
        logging.warn(f'Message from {message.author} deleted due to inappropriate content.')
    
    await bot.process_commands(message)

# Add commands to the bot
bot.add_command(kick.kick)
bot.add_command(ban.ban)
bot.add_command(warn.warn)
bot.add_command(mute.mute)

# Run the bot
bot.run(settings.DISCORD_TOKEN)