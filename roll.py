import discord
import random
import re
from discord.ext import commands

client = commands.Bot(command_prefix= "-")

def random_dice(die_amount, die):
    get_roll = [random.randint(1, die) for _ in range(die_amount)]
    print(get_roll)

    total_roll = 0
    for i in range(len(get_roll)):
        print(get_roll[i])
        total_roll += get_roll[i]

    return total_roll

@client.event
async def on_ready():
    print("Bot is ready!")

@client.command()
async def roll(ctx, user_post):
    die = 0
    die_amount = 0
    get_roll = 0
    user_request = []

    for char in user_post:
        user_request.append(char)

    new_list = [num for num in user_request if num.isdigit()]
    if len(new_list) > 3:
        die_amount = int(str(new_list[0]) + str(new_list[1]))
        die = int(str(new_list[2] + str(new_list[3])))

    elif len(new_list) > 2:
        die_amount = int(str(new_list[0]))
        die = int(str(new_list[1] + str(new_list[2])))
    else:
        die_amount = int(str(new_list[0]))
        die = int(str(new_list[1]))
        
    get_roll = random_dice(die_amount, die)
    await ctx.send(f'Rolling {die_amount}d{die}\nYou rolled: {get_roll}')


client.run('')