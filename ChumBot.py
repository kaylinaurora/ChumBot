import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging
# Grab token from .env
load_dotenv()
bot_token = os.getenv('DISCORD_BOT_TOKEN')

# Enable intents for monitoring reactions and reading messages
intents = discord.Intents.default()
intents.messages = True
intents.reactions = True
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)

# Setup logging with a higher level for console to suppress initial messages
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('chumbot.log', 'a', 'utf-8')
file_handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s', '%Y-%m-%d %H:%M:%S'))
logger.addHandler(file_handler)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)  # Initially set to ERROR to suppress info messages on console
logger.addHandler(console_handler)

@bot.event
async def on_ready():
    # After logging in, lower the console handler's level to start showing detailed logs on console
    console_handler.setLevel(logging.INFO)  # Adjust this level as needed
    logger.info(f'👾 Logged in as {bot.user.name}')

# Listen for the 🤕 reaction and trigger a DM
@bot.event
async def on_raw_reaction_add(payload):
    if str(payload.emoji) == '🤕':
        try:
            channel = await bot.fetch_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            reacting_user = bot.get_user(payload.user_id)

            # If the bot couldn't find the user in its cache, try fetching from the API.
            if reacting_user is None:
                reacting_user = await bot.fetch_user(payload.user_id)

            # Check if the reactor is the message author.
            if reacting_user != message.author:
                message_link = f"https://discord.com/channels/{message.guild.id}/{channel.id}/{message.id}"
                notification_message = f"Hello, your message received a 🤕 reaction indicating it may have been hurtful. Please be mindful of your words.\n\n**Message**:\n>>> {message.content}\n[View Message]({message_link})"

                # Check if the notification message is over 2000 characters.
                if len(notification_message) > 2000:
                    # Truncate the original message content to fit within the limit.
                    max_original_msg_length = 2000 - len(notification_message) + len(message.content) - 3
                    truncated_message_content = message.content[:max_original_msg_length] + "..."
                    notification_message = f"Hello, your message received a 🤕 reaction indicating it may have been hurtful. Please be mindful of your words.\n\n**Message**:\n>>> {truncated_message_content}\n[View Message]({message_link})"

                dm_message = await message.author.send(notification_message)
                logging.info(f"📲 DM sent to {message.author.name} by {reacting_user.name} for message {message.id}\n   {message_link}")
            
        except discord.errors.Forbidden:
            logging.warning(f"Could not send DM. User might have DMs disabled for message {payload.message_id}.")
        except Exception as e:
            logging.error(f"An error occurred while attempting to send a DM for message {payload.message_id}: {e}")

    # Check if the reaction is ❌ and if the channel is a DM.
    elif str(payload.emoji) == '❌':
        try:
            channel = bot.get_channel(payload.channel_id)
            if isinstance(channel, discord.DMChannel):
                message = await channel.fetch_message(payload.message_id)
                if message.author == bot.user:
                    await message.delete()
                    logging.info(f"❌ Message {payload.message_id} deleted by {channel.recipient}")
        except discord.NotFound:
            logging.info(f"The message {payload.message_id} was not found.")
        except discord.Forbidden:
            logging.warning(f"The bot does not have permissions to delete the message {payload.message_id}.")
        except Exception as e:
            logging.error(f"An error occurred while attempting to delete message {payload.message_id}: {e}")

# Run the bot
bot.run(bot_token)
