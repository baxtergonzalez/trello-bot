import discord
from trello_gets import *
from trello_posts import *
from ref_data import *

DISCORD_TOKEN = "OTc1NDc1OTMyOTkzMzIzMDg5.GH2JQh.gInMHme5CpKnxjmW4Jm6S1xiQXpLoXBbc489-8"

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format((client)))

def format_tasks(message, channel):
    team_list = {
        "business-sub-team" : "Business Team",
        "science-sub-team" : "Science Team",
        "engineering-sub-team" : "Engineering Team",
        "administrative-sub-team" : "Administrative"
    }

    task_list = find_cards_on_boards(team_list[channel])
    formatted_response = ""

    for task in task_list:
        formatted_response = formatted_response + "\n-" + str(task) + "\n"
        for i in range(len(task_list[task])):
            if i == 0:
                formatted_response = formatted_response + "\t" + str(task_list[task][i])
            elif i != 0:
                formatted_response = formatted_response + "\t\t-" + TEAM_LOGINS[str(task_list[task][i])]
            formatted_response = formatted_response + "\n"
    final_response = f"The {team_list[channel]} team tasks are: \n{formatted_response}"
    return final_response
            


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)

    print(f"{username} : {user_message} ({channel})")

    if message.author == client.user:
        return
    elif user_message.lower() == '!tasks':
        formatted_response = format_tasks(message, channel)
        await message.channel.send(formatted_response)
        return
    elif user_message.lower() == 'bye':
        await message.channel.send(f"See you later {username}")
        return
    elif user_message.lower() == '!random':
        response = "PeePee PooPoo"
        await message.channel.send(response)
        return


client.run(DISCORD_TOKEN)
