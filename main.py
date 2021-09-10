# Import required libraries to run
import discord
from discord.ext import commands
from discord_slash import SlashCommand
import random
import csv

from discord_slash.utils.manage_commands import create_choice, create_option
activity = discord.Activity(type=discord.ActivityType.listening, name="plexion.dev")
bot = commands.Bot(command_prefix="!", activity=activity)
slash = SlashCommand(bot, sync_commands=True)
bot.remove_command("help")

# Run on startup
@bot.event
async def on_ready():
    print ("\nEvents successfully launched!\n")

# Assign bot to a guild
guild = open("guild.txt", "r")
guild_id = [int(guild.read())]
guild.close()

# Assign channels in guild
with open('channels.txt') as doc:
    reader = csv.reader(doc, delimiter=",")
    try:
        for row in reader:
            events = int(row[0])
            updates = int(row[1])
    except IndexError:
        pass

# Bot commands
@bot.command(aliases=["create","edit","announce","query"])
async def help(ctx): #Message indicating the switch to /slash commands
    embed = discord.Embed(
        title = "That didn't work..",
        description = "The bot now handles all commands with the in-built /slash commands, type / to begin.",
        colour = 0xed5956
    )
    await ctx.send(embed = embed)

@slash.slash(
    name="create",
    description="Announces a new event",
    guild_ids=guild_id,
    options=[
        create_option(
            name="title",
            description="Specify a title for your event",
            option_type=3,
            required=True
        ),
        create_option(
            name="description",
            description="Write a summary of your event, around 50-100 words",
            option_type=3,
            required=True
        ),
        create_option(
            name="players",
            description="Specify if there's a maximum player limit or unlimited",
            option_type=3,
            required=True
        ),
        create_option(
            name="location",
            description="Specify where the event will be hosted",
            option_type=3,
            required=True
        ),
        create_option(
            name="date",
            description="What date and time will the event be hosted?",
            option_type=3,
            required=True
        ),
        create_option(
            name="status",
            description="Specify the current status of the event",
            option_type=3,
            required=True,
            choices=[
                create_choice(
                    name="Ready to start",
                    value="ready"
                ),
                create_choice(
                    name="Waiting for players",
                    value="waiting"
                ),
                create_choice(
                    name="Developing and testing",
                    value="progress"
                ),
                create_choice(
                    name="Cancelled",
                    value="cancelled"
                ),
                create_choice(
                    name="Ended",
                    value="ended"
                )
            ]
        ),
        create_option(
            name="teams",
            description="Specify if there will be teams or just solos",
            option_type=3,
            required=False
        ),
        create_option(
            name="version",
            description="Is a specific game version required?",
            option_type=3,
            required=False
        )
    ]
)
async def create(ctx, title, description, status, players, location, date, teams=None, version=None): #Custom-defined embed
    perms = ctx.author.permissions_in(ctx.channel)
    if perms.administrator:
        try:
            if status == "1" or status == "ready":
                embed = discord.Embed(
                    title = (title),
                    description = (description),
                    colour = 0x76f755
                )
                embed.set_footer(text="Ready to start!  •  React to join / if you're unsure on anything")
            elif status == "2" or status == "waiting":
                embed = discord.Embed(
                    title = (title),
                    description = (description),
                    colour = 0x7581ef
                )
                embed.set_footer(text="Waiting for some players •  React to join / if you're unsure on anything")
            elif status == "3" or status == "progress":
                embed = discord.Embed(
                    title = (title),
                    description = (description),
                    colour = 0xefda9a
                )
                embed.set_footer(text="Being actively developed & tested  •  React to join / if you're unsure on anything")
            elif status == "4" or status == "cancelled":
                embed = discord.Embed(
                    title = (title),
                    description = (description),
                    colour = 0xed5956
                )
                embed.set_footer(text="Event cancelled")
            else:
                embed = discord.Embed(
                    title = (title),
                    description = (description),
                    colour = 0xed5956
                )
                embed.set_footer(text="Event has finished, thanks for joining!")
            embed.add_field(name = f"<:players:850780580899848243> Players", value = players, inline = True)
            if teams != None:
                embed.add_field(name = "<:teams:850780581050449990> Teams", value = teams, inline = True)
            embed.add_field(name = "<:location:850780581092655144> Location", value = location, inline = True)
            embed.add_field(name = "<:date:850780581083873280> Date", value = date, inline = True)
            if version != None:
                embed.add_field(name = "<:version:885917498178953266> Version", value = version, inline = True)

            channel = bot.get_channel(events)
            message = await channel.send(embed = embed)
            await message.add_reaction("<:finished:850783040648773633>")
            await message.add_reaction("<:help:850783040174030869>")

            embed2 = discord.Embed(
                title = "Success!",
                description = "Your event has been created, try announcing by using /announce! If you need to edit the status or any other information on this event, copy the ID and use /edit.",
                colour = 0x76f755
            )
            await ctx.send(embed = embed2, hidden=True)
        except:
            embed = discord.Embed(
                title = "That didn't work..",
                description = "The command you ran is missing arguments, ensure you have: [title, description, players, teams, location, date, status]",
                colour = 0xed5956
            )
            await ctx.send(embed = embed, hidden=True)
    else:
        embed = discord.Embed(
            title = "That didn't work..",
            description = "You're lacking the required permissions for this command, run /help for more info!",
            colour = 0xed5956
        )
        await ctx.send(embed = embed, hidden=True)

@slash.slash(
    name="edit",
    description="Edits an already existing event's information",
    guild_ids=guild_id,
    options=[
        create_option(
            name="title",
            description="Specify a title for your event",
            option_type=3,
            required=True
        ),
        create_option(
            name="description",
            description="Write a summary of your event, around 50-100 words",
            option_type=3,
            required=True
        ),
        create_option(
            name="players",
            description="Specify if there's a maximum player limit or unlimited",
            option_type=3,
            required=True
        ),
        create_option(
            name="location",
            description="Specify where the event will be hosted",
            option_type=3,
            required=True
        ),
        create_option(
            name="date",
            description="What date and time will the event be hosted?",
            option_type=3,
            required=True
        ),
        create_option(
            name="status",
            description="Specify the current status of the event",
            option_type=3,
            required=True,
            choices=[
                create_choice(
                    name="Ready to start",
                    value="ready"
                ),
                create_choice(
                    name="Waiting for players",
                    value="waiting"
                ),
                create_choice(
                    name="Developing and testing",
                    value="progress"
                ),
                create_choice(
                    name="Cancelled",
                    value="cancelled"
                ),
                create_choice(
                    name="Ended",
                    value="ended"
                )
            ]
        ),
        create_option(
            name="teams",
            description="Specify if there will be teams or just solos",
            option_type=3,
            required=False
        ),
        create_option(
            name="version",
            description="Is a specific game version required?",
            option_type=3,
            required=False
        ),
        create_option(
            name="message_id",
            description="Provide the message ID (leave blank to grab the latest message)",
            option_type=3,
            required=False
        )
    ]
)
async def edit(ctx, title, description, status, players, location, date, teams=None, version=None, message_id=None): #Set event status
    perms = ctx.author.permissions_in(ctx.channel)
    if perms.administrator:
        if status == "1" or status == "ready":
                embed = discord.Embed(
                    title = (title),
                    description = (description),
                    colour = 0x76f755
                )
                embed.set_footer(text="Ready to start!  •  React to join / if you're unsure on anything")
        elif status == "2" or status == "waiting":
            embed = discord.Embed(
                title = (title),
                description = (description),
                colour = 0x7581ef
            )
            embed.set_footer(text="Waiting for some players •  React to join / if you're unsure on anything")
        elif status == "3" or status == "progress":
            embed = discord.Embed(
                title = (title),
                description = (description),
                colour = 0xefda9a
            )
            embed.set_footer(text="Being actively developed & tested  •  React to join / if you're unsure on anything")
        elif status == "4" or status == "cancelled":
            embed = discord.Embed(
                title = (title),
                description = (description),
                colour = 0xed5956
            )
            embed.set_footer(text="Event cancelled")
        else:
            embed = discord.Embed(
                title = (title),
                description = (description),
                colour = 0xed5956
            )
            embed.set_footer(text="Event has finished, thanks for joining!")
        embed.add_field(name = f"<:players:850780580899848243> Players", value = players, inline = True)
        if teams != None:
            embed.add_field(name = "<:teams:850780581050449990> Teams", value = teams, inline = True)
        embed.add_field(name = "<:location:850780581092655144> Location", value = location, inline = True)
        embed.add_field(name = "<:date:850780581083873280> Date", value = date, inline = True)
        if version != None:
            embed.add_field(name = "<:version:885917498178953266> Version", value = version, inline = True)

        channel = bot.get_channel(events)
        if message_id == None:
            message = await channel.fetch_message(channel.last_message_id)
        else:
            message = await channel.fetch_message(message_id)

        await message.edit(embed = embed)

        embed2 = discord.Embed(
            title = "Success!",
            description = "Your event has been edited with the information you entered.",
            colour = 0x76f755
        )
        await ctx.send(embed = embed2, hidden=True)
    else:
        embed = discord.Embed(
            title = "That didn't work..",
            description = "You're lacking the required permissions for this command, run /help for more info!",
            colour = 0xed5956
        )
        await ctx.send(embed = embed, hidden=True)

@slash.slash(
    name="announce",
    description="Pings an announcement for a new event",
    guild_ids=guild_id,
    options=[
        create_option(
            name="title",
            description="Specify the title of the event you want to announce",
            option_type=3,
            required=True
        ),
    ]
)
async def announce(ctx, title): #Set event status
    perms = ctx.author.permissions_in(ctx.channel)
    if perms.administrator:
        channel = bot.get_channel(updates)
        await channel.send(f"@everyone A **{title}** event has been announced, go react in <#{events}>!")

        embed2 = discord.Embed(
            title = "Success!",
            description = "Your event has been announced based on the title you entered.",
            colour = 0x76f755
        )
        await ctx.send(embed = embed2, hidden=True)
    else:
        embed = discord.Embed(
            title = "That didn't work..",
            description = "You're lacking the required permissions for this command, run /help for more info!",
            colour = 0xed5956
        )
        await ctx.send(embed = embed, hidden=True)

@slash.slash(name="help", description="Lists all commands available, depending on the author's permissions", guild_ids=guild_id)
async def help(ctx): #HELP MSG
    perms = ctx.author.permissions_in(ctx.channel)
    if perms.administrator:
        embed = discord.Embed(
            title = "All commands",
            description = "Here is every command available to you, based on your permissions:",
            colour = 0x3359f2
            )
        embed.set_footer(text="The bot is now linked in with discord slash commands, simply type / to get started.")
        embed.add_field(name = "<:add:850825248507953172> create", value = "Announces a new event", inline = False)
        embed.add_field(name = "<:edit:850825297301209108> edit", value = "Edits an already existing event's information", inline = False)
        embed.add_field(name = "<:announce:850827849153642547> announce", value = "Pings an announcement for a new event", inline = False)
        embed.add_field(name = "<:query:850920584081571880> query", value = "Will query who has reacted to an event", inline = False)
        embed.add_field(name = "<:help:850783040174030869> help", value = "Lists all commands available, depending on the author's permissions", inline = False)

        await ctx.send(embed = embed, hidden=True)
    else:
        embed = discord.Embed(
            title = "All commands",
            description = "Here is every command available to you, based on your permissions:",
            colour = 0x3359f2
            )
        embed.add_field(name = "<:help:850783040174030869> /help", value = "Lists all commands available, depending on the author's permissions", inline = False)
        embed.set_footer(text="The bot is now linked in with discord slash commands, simply type / to get started.")

        await ctx.send(embed = embed, hidden=True)

@slash.slash(
    name="query",
    description="Will query who has reacted to an event",
    guild_ids=guild_id,
    options=[
        create_option(
            name="message_id",
            description="Provide the message ID (leave blank to grab the latest message)",
            option_type=3,
            required=False
        )
    ]
)
async def query(ctx, message_id=None): #TEST EMBED
    perms = ctx.author.permissions_in(ctx.channel)
    if perms.administrator:
        channel = bot.get_channel(events)

        embed = discord.Embed(
            title = "Event Reactions",
            description = "Here is the list of people who have reacted for this event:",
            colour = 0x3359f2
            )
        embed.set_footer(text="This message is static and will need to be called again if anything changes.")
        if message_id == None:
            message = await channel.fetch_message(channel.last_message_id)
        else:
            message = await channel.fetch_message(message_id)
        for reaction in message.reactions:
            users1 = []
            users2 = []
            available = []
            unsure = []
            if str(reaction) == "<:finished:850783040648773633>" or str(reaction) == "<:finished:809552632485904405>":
                users = await reaction.users().flatten()
                users1.extend(users)
                available = str(', '.join(f"<@{user.id}>" for user in users1))
                embed.add_field(name = "<:finished:850783040648773633> Available", value = available, inline = False)

            elif str(reaction) == "<:help:850783040174030869>" or str(reaction) == "<:help:826918595241967627>":
                users = await reaction.users().flatten()
                users2.extend(users)
                unsure = str(', '.join(f"<@{user.id}>" for user in users2))
                embed.add_field(name = "<:help:850783040174030869> Reserves/Unsure", value = unsure, inline = False)

        message = await ctx.send(embed = embed, hidden=True)
    else:
        embed = discord.Embed(
            title = "That didn't work..",
            description = "You're lacking the required permissions for this command, run /help for more info!",
            colour = 0xed5956
        )
        await ctx.send(embed = embed, hidden=True)

# Run bot using token
token = open("token.txt", "r")
bot.run(token.read())
token.close()