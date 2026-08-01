import discord
from discord.ext import commands
import os

# Configuration: Replace these with actual Role IDs and Channel ID
# These can be loaded from .env in production
REACTION_CHANNEL_ID = 123456789012345678  # Replace with the actual #choose-your-roles channel ID
MESSAGE_ID = None  # We will store the message ID of the reaction menu here

# Emoji to Role ID mapping
# Add the actual role IDs created in the Discord server
ROLE_MAPPING = {
    "🇺🇸": 111111111111111111,  # English role ID
    "🇪🇸": 222222222222222222,  # Espanol role ID
    "🇫🇷": 333333333333333333,  # Francais role ID
    "💻": 444444444444444444,  # Developer role ID
    "📈": 555555555555555555   # Industry Interest role ID
}

intents = discord.Intents.default()
intents.reactions = True
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.command()
@commands.has_permissions(administrator=True)
async def setup_roles(ctx):
    """Admin command to spawn the reaction role message in the designated channel."""
    channel = bot.get_channel(REACTION_CHANNEL_ID)
    if not channel:
        await ctx.send("Error: Reaction channel not found. Check REACTION_CHANNEL_ID.")
        return

    text = (
        "**Choose your roles by reacting below!**\n\n"
        "**Languages:**\n"
        "🇺🇸 English\n"
        "🇪🇸 Español\n"
        "🇫🇷 Français\n\n"
        "**Other Roles:**\n"
        "💻 Developer\n"
        "📈 Industry Interest\n"
    )
    
    msg = await channel.send(text)
    
    # Add initial reactions
    for emoji in ROLE_MAPPING.keys():
        await msg.add_reaction(emoji)
        
    global MESSAGE_ID
    MESSAGE_ID = msg.id
    await ctx.send("Reaction roles menu set up successfully!")

@bot.event
async def on_raw_reaction_add(payload):
    """Triggered when a user adds a reaction to any message."""
    if payload.message_id != MESSAGE_ID:
        return
        
    if payload.member.bot:
        return

    guild = bot.get_guild(payload.guild_id)
    role_id = ROLE_MAPPING.get(str(payload.emoji))
    
    if role_id:
        role = guild.get_role(role_id)
        if role:
            await payload.member.add_roles(role)
            print(f"Assigned {role.name} to {payload.member.display_name}")

@bot.event
async def on_raw_reaction_remove(payload):
    """Triggered when a user removes a reaction from any message."""
    if payload.message_id != MESSAGE_ID:
        return

    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    
    if not member:
        return

    role_id = ROLE_MAPPING.get(str(payload.emoji))
    
    if role_id:
        role = guild.get_role(role_id)
        if role:
            await member.remove_roles(role)
            print(f"Removed {role.name} from {member.display_name}")

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_BOT_TOKEN")
    if not TOKEN:
        print("Error: DISCORD_BOT_TOKEN environment variable not set.")
    else:
        bot.run(TOKEN)